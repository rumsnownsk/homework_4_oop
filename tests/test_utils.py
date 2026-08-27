import json
import os
import tempfile
from typing import Any, Dict, List

import pytest

from src.category import Category
from src.utils import created_objects_from_json, read_json


@pytest.fixture
def json_data() -> List[Dict[str, Any]]:
    return [
        {
            "name": "Фрукты",
            "description": "Спелые фрукты",
            "products": [
                {"name": "Яблоко", "description": "Зелёное", "price": 80.0, "quantity": 10},
                {"name": "Банан", "description": "Жёлтый", "price": 60.0, "quantity": 20},
            ],
        },
        {
            "name": "Молочка",
            "description": "Молочные продукты",
            "products": [{"name": "Молоко", "description": "Пастеризованное", "price": 90.0, "quantity": 30}],
        },
    ]


def test_read_json(json_data: List[Dict[str, Any]]):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as tmp_file:
        json.dump(json_data, tmp_file)
        tmp_path = tmp_file.name

    try:
        result = read_json(tmp_path)
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["name"] == "Фрукты"
    finally:
        os.unlink(tmp_path)

    # если файла такого не обнаружено возращает пустой список
    result_no_file = read_json("no_file.json")
    assert result_no_file == []


def test_read_json_invalid_json():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        tmp.write("{ невалидный json }")
        tmp_path = tmp.name

    try:
        result = read_json(tmp_path)
        assert result == []
    finally:
        os.unlink(tmp_path)


def test_read_json_not_list():
    not_list = {"data": "not list"}

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        json.dump(not_list, tmp)
        tmp_path = tmp.name
    try:
        res = read_json(tmp_path)
        assert res == []
    finally:
        os.unlink(tmp_path)


def test_created_objects_success(json_data: List[Dict[str, Any]]):
    categories, products = created_objects_from_json(json_data)

    # Проверяем типы
    assert isinstance(categories, list)
    assert isinstance(products, list)

    # Количество категорий и продуктов
    assert len(categories) == 2
    assert len(products) == 3  # 2 + 1

    # Проверка категорий
    cat1, cat2 = categories
    assert isinstance(cat1, Category)
    assert cat1.name == "Фрукты"
    assert cat1.description == "Спелые фрукты"

    assert isinstance(cat2, Category)
    assert cat2.name == "Молочка"
