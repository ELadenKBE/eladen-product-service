from django.db.models import QuerySet, Q
from graphql import GraphQLResolveInfo

from goods.models import Good
from goods_list.models import GoodsList
from productService.errors import UnauthorizedError, ResourceError
from productService.repository_base import RepositoryBase, IRepository
from users.models import ExtendedUser


class GoodsListRepository(RepositoryBase, IRepository):

    model = GoodsList

    @staticmethod
    def create_item(info: GraphQLResolveInfo = None, **kwargs) -> [QuerySet]:
        user = info.context.user or None
        if user is None:
            raise UnauthorizedError("Unauthorized access!")
        good_list = GoodsList(title=kwargs["title"], user_id=user.id)
        good_list.save()
        return good_list

    @staticmethod
    def get_all_items(info: GraphQLResolveInfo = None) -> [QuerySet]:
        """
                TODO docstring

                :param info:
                :return:
                """
        user: ExtendedUser = info.context.user
        if user.is_user() or user.is_seller():
            return GoodsList.objects.filter(user_id=user.id).all()
        if user.is_admin():
            return GoodsList.objects.all()

    @staticmethod
    def get_items_by_filter(search_filter: Q,
                            info: GraphQLResolveInfo = None) -> [QuerySet]:
        """
                TODO docstring

                :param search_filter:
                :param info:
                :return:
                """
        user: ExtendedUser = info.context.user
        search_filter = (Q(title__icontains=search_filter))
        filtered_list = GoodsList.objects.filter(search_filter).all()
        lists_to_return = []
        for item in filtered_list:
            if int(item.user_id) == int(user.id):
                lists_to_return.append(item)
        return lists_to_return

    @staticmethod
    def get_by_id(searched_id: str,
                  info: GraphQLResolveInfo = None) -> [QuerySet]:
        """
                TODO docstring

                :param searched_id:
                :param info:
                :return:
                """
        user: ExtendedUser = info.context.user
        if user.is_admin():
            return GoodsList.objects.filter(id=searched_id).first()
        if user.is_user() or user.is_seller():
            return GoodsList.objects.filter(id=searched_id,
                                            user_id=user.id).first()

    @staticmethod
    def add_good_to_cart(info: GraphQLResolveInfo, good_id: str):
        """
                TODO add doctrings

                :param info:
                :param good_id:
                :return: a good added to cart
                """
        user = info.context.user or None
        if user is None:
            raise UnauthorizedError("Unauthorized access!")
        good = Good.objects.get(id=good_id)
        cart_list: GoodsList = GoodsList.objects.filter(user_id=user.id,
                                                        title="cart").first()
        if good is None:
            raise ResourceError('good with this id does not exist')
        if cart_list is None:
            raise ResourceError('cart for this user does not exist')
        cart_list.goods.add(good)
        cart_list.save()
        return good

    @staticmethod
    def clean_goods(info: GraphQLResolveInfo, list_id: str):
        """
                TODO add doctrings

                :param info:
                :param list_id:
                :return:
                """
        goods_list = GoodsList.objects.filter(id=list_id).first()
        user: ExtendedUser = info.context.user
        if user.is_admin():
            goods_list.goods.clear()
            goods_list.save()
        elif user.is_seller() or user.is_user():
            if goods_list.user_id == user.id:
                goods_list.goods.clear()
                goods_list.save()
            else:
                raise UnauthorizedError(
                    "Not enough permissions to call this endpoint")
        return goods_list

    @staticmethod
    def update_item(info: GraphQLResolveInfo, item_id, **kwargs) -> [QuerySet]:
        """
                TODO add docstr

                :param item_id:
                :param info:
                :param title:
                :return:
                """
        goods_list: GoodsList = GoodsList.objects.filter(id=item_id).first()
        user: ExtendedUser = info.context.user
        if user.is_admin():
            goods_list.title = kwargs["title"]
        elif user.is_user() or user.is_seller():
            if goods_list.user_id == user.id:
                goods_list.title = kwargs["title"]
            else:
                raise UnauthorizedError(
                    "Not enough permissions to call this endpoint")
        goods_list.save()
        return goods_list

    @staticmethod
    def delete_item(info: GraphQLResolveInfo, searched_id: str):
        """
                TODO add docs

                :param searched_id:
                :param info:
                :return:
                """
        goods_list = GoodsList.objects.filter(id=searched_id).first()
        if goods_list is None:
            raise ResourceError('object with searched id does not exist')
        user: ExtendedUser = info.context.user
        if user.is_admin():
            goods_list.delete()
        elif (user.is_seller() or user.is_user())\
                and goods_list.user_id == user.id:
            goods_list.delete()
        else:
            raise UnauthorizedError(
                "Not enough permissions to call this endpoint")

    @staticmethod
    def change_category(info: GraphQLResolveInfo,
                        searched_id: str,
                        category_id: str) -> [QuerySet]:
        pass

