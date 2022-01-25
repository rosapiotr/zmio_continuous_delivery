import pytest
from wallet import Wallet, InsufficientAmount
import entity.product
import repository.product_repository
import service.product_service


def test_product_init():
    product = entity.product.Product("10", "bmw", "130000", "siema")
    assert product.name == "bmw"
