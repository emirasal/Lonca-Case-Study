import re
import xml.etree.ElementTree as ET

class Product:
    def __init__(self, product_element):
        self.product_element = product_element
        self.product_id = product_element.attrib['ProductId']
        self.name = self.format_product_name(product_element.attrib['Name'])
        self.images = self.extract_images(product_element)
        self.description = self.format_description(product_element.find('Description').text)
        self.product_details = self.extract_product_details(product_element.find('ProductDetails'))

    # Capitalizing the first letter
    def format_product_name(self, name):
        return name.capitalize()

    # Rremoving extra spaces and HTML tags
    def format_description(self, description):
        if description:
            cleaned_description = re.sub(r'<.*?>', '', description)
            return re.sub(r'\s+', ' ', cleaned_description.strip())
        return ""

    def extract_product_details(self, details_element):
        details = {}
        if details_element:
            for detail in details_element.findall('ProductDetail'):
                name = detail.attrib['Name']
                value = detail.attrib['Value']
                
                details[name] = value
        return details

    def to_dict(self):
        return {
            "ProductId": self.product_id,
            "Name": self.name,
            "Images": self.images,
            "Description": self.description,
            "ProductDetails": self.product_details
        }
