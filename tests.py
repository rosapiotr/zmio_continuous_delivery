import pytest
from entity.product import Product
from repository.product_repository import ProductRepository
from service.product_service import ProductService



def test_product_init():
    product = Product("10", "BMW", "130000", "BMW Maciej")
    assert product.name == "BMW"

def test_get_product():
    productRepo = ProductRepository()
    product1 = productRepo.get_product("1")
    assert product1.name == "Volkswagen Polo"