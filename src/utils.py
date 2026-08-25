import json
import os.path

from src.category import Category
from src.product import Product


def read_json(path:str) -> list:
    full_path = os.path.abspath(path)
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def created_objects_from_json(raw_data):
    categories = []
    products = []

    for category_raw in raw_data:
        category_products = []

        for product_raw in category_raw["products"]:
            product_obj = Product(**product_raw)
            products.append(product_obj)
            category_products.append(product_obj)

        category_obj = Category(
            name=category_raw["name"],
            description=category_raw.get("description", ""),
            products=category_products
        )
        categories.append(category_obj)

    return categories, products

