import random
import uuid
from itertools import count
from typing import List
from django.utils.text import slugify
from tqdm import tqdm
from faker import Faker
from warehouse.models import Product, Brand, Category, Tag, Pack, AttributeValue
from painless.repository.generator import BaseDataGenerator

fake = Faker()


class WarehouseDataGenerator(BaseDataGenerator):
    """
    A class responsible for generating fake data for warehouse tables.
    Inherits from BaseDataGenerator for data generation utilities.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the WarehouseDataGenerator.

        Attributes:
            priority_counter (itertools.count): A counter that generates
            sequential priority values for generated data.
        """
        super().__init__(*args, **kwargs)
        self.priority_counter = count(start=1)

    def create_products(
        self, total: int = 200, batch_size: int = 10, disable_progress_bar: bool = False
    ) -> List[Product]:
        """
        Generate and create fake products.

        Args:
            total (int): The total number of products to create. Default is 5.
            batch_size (int): The number of products to create per batch. Default is 10.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Product]: A list of created products.
        """
        tags = list(Tag.objects.all())

        products = [
            Product(
                title=words,
                slug=slugify(words),
                subtitle=self.get_random_text(1),
                can_review=self.get_random_bool(),
                is_active=self.get_random_bool(),
                brand=self.get_random_brands(),
                category=self.get_random_categories(),
                min_purchase=random.randint(1, 5),
                max_purchase=random.randint(5, 20),
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
            if (words := f"product {_} {self.get_random_words(1)}")
        ]

        created_products = Product.objects.bulk_create(products)

        for product in created_products:
            product.tags.set(random.sample(tags, k=min(3, len(tags))))
            related_products = random.sample(
                list(Product.objects.exclude(pk=product.pk)), k=min(3, Product.objects.count() - 1)
            )
            product.related_products.set(related_products)
            suggested_products = random.sample(
                list(Product.objects.exclude(pk=product.pk)), k=min(3, Product.objects.count() - 1)
            )
            product.suggested_products.set(suggested_products)

        return created_products

    def create_brands(
        self, total: int = 200, batch_size: int = 10, disable_progress_bar: bool = False
    ) -> List[Brand]:
        """
        Generate and create fake brands.

        Args:
            total (int): The total number of brands to create. Default is 200.
            batch_size (int): The number of brands to create per batch. Default is 10.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Brand]: A list of created brands.
        """
        brands = [
            Brand(
                title=words,
                slug=slugify(words),
                subtitle=words + self.get_random_text(1),
                is_active=self.get_random_bool(),
                picture=fake.image_url()  # Adjust as needed for image URLs
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
            if (words := f"brand {_} {self.get_random_words(1)}")
        ]
        return Brand.objects.bulk_create(brands)

    def create_categories(
        self, total: int = 70, batch_size: int = 10, disable_progress_bar: bool = False
    ) -> List[Category]:
        """
        Generate and create fake categories.

        Args:
            total (int): The total number of categories to create. Default is 100.
            batch_size (int): The number of categories to create per batch. Default is 10.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Category]: A list of created categories.
        """
        categories = [
            Category(
                title=words,
                slug=slugify(words),
                is_active=self.get_random_bool(),
                is_downloadable=self.get_random_bool(),
                parent=None  # ! TODO
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
            if (words := f"category {_} {self.get_random_words(1)}")
        ]
        created_categories = Category.objects.bulk_create(categories)

        # Assign some categories as children of others
        for category in created_categories:
            if random.choice([True, False]):  # Randomly assign parents
                parent_category = random.choice(
                    [cat for cat in created_categories if cat != category]
                )
                category.parent = parent_category
                category.save()

        return created_categories

    def create_attribute_values(
        self, total: int = 150, batch_size: int = 10, disable_progress_bar: bool = False
    ) -> List[AttributeValue]:
        """
        Generate and create fake attribute values.

        Args:
            total (int): The total number of attribute values to create. Default is 150.
            batch_size (int): The number of attribute values to create per batch. Default is 10.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[AttributeValue]: A list of created attribute values.
        """
        attribute_values = [
            AttributeValue(
                attval_title=words,
                parent=None  # ! TODO
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
            if (words := f"attribute {_} {self.get_random_words(1)}")
        ]
        created_attribute_values = AttributeValue.objects.bulk_create(attribute_values)

        for attr_value in created_attribute_values:
            if random.choice([True, False]):  # Randomly assign parents
                parent_attr_value = random.choice(
                    [attr for attr in created_attribute_values if attr != attr_value]
                )
                attr_value.parent = parent_attr_value
                attr_value.save()

        return created_attribute_values

    def create_packs(
        self, total: int = 200, batch_size: int = 10, disable_progress_bar: bool = False
    ) -> List[Pack]:
        """
        Generate and create fake packs.

        Args:
            total (int): The total number of packs to create. Default is 200.
            batch_size (int): The number of packs to create per batch. Default is 10.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Pack]: A list of created packs.
        """

        packs = [
            Pack(
                sku=uuid.uuid4(),
                price=fake.random_number(digits=5),
                description=self.get_random_text(4),
                buy_price=fake.random_number(digits=5),
                stock=fake.random_number(digits=3),
                actual_stock=fake.random_number(digits=3),
                is_active=self.get_random_bool(),
                is_default=self.get_random_bool(),
                product=self.get_random_products(),
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]

        created_packs = Pack.objects.bulk_create(packs)

        attribute_values = list(AttributeValue.objects.all())
        for pack in created_packs:
            pack.att_val_ids.set(random.sample(attribute_values, k=min(3, len(attribute_values))))

        return created_packs
