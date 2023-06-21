# Product Microservice

This is a Django GraphQL API microservice that provides functionality for managing products. It includes packages/entities for categories, goods, and goods lists.

## Installation
Clone the repository:
```
shell


git clone https://github.com/ELadenKBE/eladen-product-service.git
```
Navigate to the project directory:
```
shell

cd product-microservice
```
Install the required dependencies using pip:

```
shell

pip install -r requirements.txt
```
Set up the database:
```
shell

python manage.py migrate
```
Start the development server:
```
shell

python manage.py runserver
```
The server should now be running at http://localhost:8000.

## GraphQL API
The Product Microservice provides a GraphQL API for querying and mutating data. The GraphQL endpoint is located at http://localhost:8000/graphql.

To explore and interact with the API, you can use tools like GraphiQL or Insomnia.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.