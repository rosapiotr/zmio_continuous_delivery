from flask import Flask
from repository.product_repository import ProductRepository

app = Flask(__name__)

class ProductService:

    def __init__(self):
        self.products_repo = ProductRepository()

    def get_product(self, id):
        app.logger.debug("Getting product " + str(id) + "...")
        product = self.products_repo.get_product(id)
        return product
