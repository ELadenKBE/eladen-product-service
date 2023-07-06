from django.contrib.auth.models import AnonymousUser
from graphql import GraphQLError
from django.contrib.auth import authenticate

from productService.user_service import UserService
from users.models import ExtendedUser

user_service = UserService()


def get_user_id(context) -> int:
    pass


class CustomAuthenticationMiddleware:
    def resolve(self, next, root, info, **kwargs):
        context = info.context
        user_id = get_user_id(context)
        user: ExtendedUser = user_service.get_user(user_id)
        if user is not None:
            context.user = user
        else:
            context.user = AnonymousUser()
