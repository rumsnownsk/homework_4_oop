import json
import os.path

from src.category import Category
from src.product import Product


def read_json(path:str) -> dict:
    full_path = os.path.abspath(path)

    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def created_objects_from_json(raw_data):
    categories = []
    products = []

    for category in raw_data:
        for product in category["products"]:
            products.append(Product(**product))
        categories.append(Category(**category))

    return categories, products

