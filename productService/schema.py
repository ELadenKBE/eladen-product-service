import graphene
import graphql_jwt

import category.schema
import goods.schema
import goods_list.schema
import users.schema


class Query(users.schema.Query,
            goods.schema.Query,
            category.schema.Query,
            goods_list.schema.Query,
            graphene.ObjectType):
    pass


class Mutation(goods.schema.Mutation,
               users.schema.Mutation,
               category.schema.Mutation,
               goods_list.schema.Mutation,
               graphene.ObjectType,):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)