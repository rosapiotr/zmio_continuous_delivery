from flask import Flask

from entity.product import Product

app = Flask(__name__)

class ProductRepository:

    def __init__(self):
        product_1 = Product("0", "Audi A6", "60000", "BMW")
        product_2 = Product("1", "Volkswagen Polo", "25000", "Volkswagen")
        product_3 = Product("2", "Alfa Romeo Giulia", "70000", "Alfa Romeo")
        product_4 = Product("3", "Peugeot 306", "20000", "Peugeot")

        self.db = [product_1, product_2, product_3, product_4]

    def get_product(self, id):
        return self.db[int(id)]
