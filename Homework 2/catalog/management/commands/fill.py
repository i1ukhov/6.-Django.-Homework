import os
from django.core.management import BaseCommand
import json
from config.settings import FIXTURES_ROOT
from catalog.models import Category, Product

filename = "catalog_data.json"
file_path = os.path.join(FIXTURES_ROOT, filename)


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        """Чтение данных из фикстуры с категориями"""
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            categories = []
            for item in data:
                if item["model"].split(".")[1] == "category":
                    categories.append(item)
            return categories

    @staticmethod
    def json_read_products():
        """Получение данных из фикстуры с продуктами"""
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            products = []
            for item in data:
                if item["model"].split(".")[1] == "product":
                    products.append(item)
            return products

    def handle(self, *args, **options):
        print(Command.json_read_products())
        print()
        print(Command.json_read_categories())
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    pk=category["pk"],
                    name=category["fields"]["name"],
                    description=category["fields"]["description"],
                )
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    image=product["fields"]["image"],
                    category=Category.objects.get(pk=product['fields']['category']),
                    price=product["fields"]["price"],
                    created_at=product["fields"]["created_at"],
                    updated_at=product["fields"]["updated_at"],
                )
            )
        Product.objects.bulk_create(product_for_create)