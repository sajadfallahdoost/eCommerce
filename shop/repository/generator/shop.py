import random
from typing import List
from itertools import count
import uuid
from django.contrib.auth.models import User
from faker import Faker
from tqdm import tqdm
from django.utils.text import slugify
from warehouse.models import Pack
from shop.models import Cart, Order, OrderAddress, CartItem
from painless.repository.generator import BaseDataGenerator
from shop.helper import TRANSACTION_STATUS

fake = Faker()


class ShopDataGenerator(BaseDataGenerator):
    """
    A class responsible for generating fake data for shop-related tables.
    Inherits from BaseDataGenerator for data generation utilities.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the ShopDataGenerator.

        Attributes:
            priority_counter (itertools.count): A counter that generates
            sequential priority values for generated data.
        """
        super().__init__(*args, **kwargs)
        self.priority_counter = count(start=1)


    def create_order_addresses(self, total: int = 100, disable_progress_bar: bool = False) -> List[OrderAddress]:
        """
        Generate and create fake order addresses.

        Args:
            total (int): The total number of order addresses to create. Default is 100.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[OrderAddress]: A list of created order addresses.
        """
        order_addresses = [
            OrderAddress(
                title=words,
                slug=slugify(words),
                country=fake.country(),
                province=fake.state(),
                city=fake.city(),
                postal_address=fake.address(),
                postal_code=fake.postcode(),
                house_number=self.get_random_int(1, 100),
                building_unit=self.get_random_int(1, 100),
                footnote=self.get_random_string(10),
                receiver_first_name=fake.first_name(),
                receiver_last_name=fake.last_name(),
                receiver_phone_number=self.get_random_phone_number(),
                receiver_national_code=1,
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
            if (words := f"order address {_} {self.get_random_words(1)}")
        ]
        return OrderAddress.objects.bulk_create(order_addresses)

    def create_carts(self, total: int = 100, disable_progress_bar: bool = False) -> List[Cart]:
        """
        Generate and create fake carts.

        Args:
            total (int): The total number of carts to create. Default is 100.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Cart]: A list of created carts.
        """

        carts = [
            Cart(
                user=self.get_random_user()
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return Cart.objects.bulk_create(carts)

    def create_orders(self, total: int = 100, disable_progress_bar: bool = False) -> List[Order]:
        """
        Generate and create fake orders.

        Args:
            total (int): The total number of orders to create. Default is 100.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Order]: A list of created orders.
        """

        orders = [
            Order(
                transaction_number=uuid.uuid4(),
                total_price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                status=random.choice([status[0] for status in TRANSACTION_STATUS]),
                order_address=self.get_random_order_address(),
                user=self.get_random_user(),
                cart=self.get_random_cart()
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return Order.objects.bulk_create(orders)

    def create_cart_items(self, total: int = 100, disable_progress_bar: bool = False) -> List[CartItem]:
        """
        Generate and create fake cart items.

        Args:
            total (int): The total number of cart items to create. Default is 100.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[CartItem]: A list of created cart items.
        """

        cart_items = [
            CartItem(
                cart=self.get_random_cart(),
                pack=self.get_random_pack(),
                quantity=self.get_random_int(0, 100)
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return CartItem.objects.bulk_create(cart_items)
