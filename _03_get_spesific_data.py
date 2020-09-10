import requests,json

req =  requests.get('https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json')
products = req.json()

output_dict = [product for product in products if product['category'] == 'fruits']

output_json = json.dumps(output_dict,indent=4)
print(output_json)