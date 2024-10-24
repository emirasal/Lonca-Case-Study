from pymongo import MongoClient
import xml.etree.ElementTree as ET
from product import Product


client = MongoClient("mongodb+srv://dbUser:dbUserPassword@cluster0.l16sj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['product_db']  
collection = db['products'] 

# Parsing
tree = ET.parse('lonca-sample.xml')
root = tree.getroot()


for product_element in root.findall('Product'):
    product = Product(product_element)
    collection.insert_one(product.to_dict())  # Inserting into MongoDB

print("Data inserted.")
