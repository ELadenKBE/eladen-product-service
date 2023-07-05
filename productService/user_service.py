import requests
from decouple import config

from productService.base_service import BaseService
from users.models import ExtendedUser


class UserService(BaseService):

    url = config('USER_SERVICE_URL', default=False, cast=str)
    service_name = 'User'

    def get_user(self, user_id):
        """

        :param info:
        :return:
        """
        query_template = """query{{
                  users(searchedId: {0}){{
                            id
                            username
                            email
                            role
                            address
                            firstName
                            lastName
                      }}
                }}"""

        query = query_template.format(int(user_id))
        response = requests.post(self.url, data={'query': query})
        data = response.json().get('data', {})
        pass