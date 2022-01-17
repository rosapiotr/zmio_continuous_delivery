from flask import Flask
from service.product_service import ProductService

app = Flask(__name__)

product_service = ProductService()

@app.route('/product/<id>')
def get_product(id):
    response = product_service.get_product(id)
    return response.to_json()


if __name__ == "__main__":
    app.run(debug=True)
