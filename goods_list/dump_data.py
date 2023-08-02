import json

from goods.models import Good


def read_product_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


# Usage example:
def add_data_to_good_model(data):
    for item in data:
        good = Good(
            id=item['id'],
            title=item['title'],
            description=item['description'],
            category_id=1,
            price=item['price'],
            image=item['image'],
            manufacturer=item['manufacturer'],
            amount=item['amount'],
            seller_id=1
            # Add other fields as required
        )
        good.save()


# Usage example:
filename = 'productdata.json'
product_dict = read_product_data(filename)
add_data_to_good_model(product_dict)