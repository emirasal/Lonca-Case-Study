from pymongo import MongoClient
import xml.etree.ElementTree as ET
from product import Product

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(mongo_uri)

db = client['product_db']  
collection = db['products'] 

# Parsing
tree = ET.parse('lonca-sample.xml')
root = tree.getroot()


for product_element in root.findall('Product'):
    product = Product(product_element)
    collection.insert_one(product.to_dict())  # Inserting into MongoDB

print("Data inserted.")
