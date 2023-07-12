import graphene

import category.schema
import goods.schema
import goods_list.schema


class Query(goods.schema.Query,
            category.schema.Query,
            goods_list.schema.Query,
            graphene.ObjectType):
    pass


class Mutation(goods.schema.Mutation,
               category.schema.Mutation,
               goods_list.schema.Mutation,
               graphene.ObjectType,):
    pass
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
