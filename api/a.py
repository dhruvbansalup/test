# import data from data.json and inventory value by category
import json

json_file = open('data.json')
data = json.load(json_file)

products = data['products']

def inventory_value_by_category(products):
    inventory_value = {}
    count_by_category = {}
    for product in products:
        category = product['category']
        price = product['price']
        quantity = product['stock']
        count_by_category[category] = count_by_category.get(category, 0) + 1
        value = price * quantity
        if category in inventory_value:
            inventory_value[category] += value
        else:
            inventory_value[category] = value
    return inventory_value, count_by_category

if __name__ == "__main__":
    inventory_value, count_by_category = inventory_value_by_category(products)
    print(inventory_value)
    print(count_by_category)