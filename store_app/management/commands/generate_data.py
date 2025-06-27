from django.core.management.base import BaseCommand
from store_app.models import Category, Product
import random
import factory
from decimal import Decimal


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('sentence')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('catch_phrase')
    description = factory.Faker('paragraph')
    price = factory.LazyFunction(lambda: Decimal(round(random.uniform(10, 1000), 2)))
    category = factory.SubFactory(CategoryFactory)


class Command(BaseCommand):
    help = 'Генерирует тестовые данные для Category и Product'

    def add_arguments(self, parser):
        parser.add_argument('--categories', type=int, default=5, help='Количество категорий')
        parser.add_argument('--products', type=int, default=20, help='Количество продуктов')

    def handle(self, *args, **kwargs):
        categories_count = kwargs['categories']
        products_count = kwargs['products']

        self.stdout.write(f"Создаем {categories_count} категорий...")
        categories = [CategoryFactory() for _ in range(categories_count)]

        self.stdout.write(f"Создаем {products_count} продуктов...")
        products = [ProductFactory(category=random.choice(categories)) for _ in range(products_count)]

        self.stdout.write(self.style.SUCCESS("✅ Данные успешно созданы!"))