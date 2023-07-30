import requests
from decouple import config
from graphene_django import DjangoObjectType

from productService.base_service import BaseService
from productService.errors import ResponseError
from users.models import ExtendedUser


class UserType(DjangoObjectType):
    class Meta:
        model = ExtendedUser


class UserService(BaseService):
    # url = config('USER_SERVICE_URL',
    #              default="http://user-identity:8081/graphql/", cast=str)
    url = "http://user-identity:8081/graphql/"
    service_name = 'User'

    def get_user_auth(self, sub: str):
        """

        :param sub:
        :return:
        """
        self.verify_connection()
        query_template = """query{{
                  users(sub: "{0}"){{
                            id
                            username
                            email
                            role
                            address
                            firstName
                            lastName
                            sub
                      }}
                }}"""

        query = query_template.format(sub)
        response = requests.post(self.url, data={'query': query})
        user_in_dict = response.json().get('data', {}).get('users')[0]
        if user_in_dict is None:
            raise ResponseError('User not found')
        user = ExtendedUser(**user_in_dict)
        return user

