# import data from data.json and inventory value by category
import json

json_file = open('data.json')
data = json.load(json_file)

products = data['products']

def inventory_value_by_category(products):
    inventory_value = {}
    for product in products:
        category = product['category']
        price = product['price']
        quantity = product['stock']
        value = price * quantity
        if category in inventory_value:
            inventory_value[category] += value
        else:
            inventory_value[category] = value
    return inventory_value

if __name__ == "__main__":
    inventory_value = inventory_value_by_category(products)
    print(inventory_value)