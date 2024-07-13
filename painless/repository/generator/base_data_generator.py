import random
import string
import uuid
from datetime import datetime

import pytz
from mimesis import Datetime, File, Generic, Text
from mimesis.locales import Locale

from warehouse.models.product import Product
from warehouse.models.brand import Brand
from warehouse.models.category import Category
from warehouse.models.pack import Pack
from warehouse.models.attribute_value import AttributeValue
from account.models import CorporateProfile, PersonalProfile
from django.contrib.auth.models import User
from shop.models.cart import Cart
from shop.models.order_address import OrderAddress


class BaseDataGenerator:
    """
    A base class for generating various types of fake data.

    Args:
        locale (str, optional): Locale code for generating data.
            Defaults to "en".

    Attributes:
        generic (Generic): Instance of Generic for generating generic data.
        text (Text): Instance of Text for generating text data.
        date_time (Datetime): Instance Datetime for generating datetime data.
        file (File): Instance of File for generating file-related data.
    """
    def __init__(self, locale: str = "en") -> None:
        """
        Initialize the BaseDataGenerator instance with the given locale.

        Args:
            locale (str, optional): Locale code for generating data.
                Defaults to "en".
        """
        self.generic = Generic(getattr(Locale, locale.upper()))
        self.text = Text(getattr(Locale, locale.upper()))
        self.date_time = Datetime(getattr(Locale, locale.upper()))
        self.file = File()

    def get_random_words(self, qty: int = 2) -> str:
        """
        Generate and return a string containing random words.

        Args:
            qty (int, optional): The number of words to generate.
                Defaults to 2.

        Returns:
            str: A string containing randomly generated words.
        """
        return " ".join(self.text.words(quantity=qty))

    def get_random_text(self, qty: int = 2) -> str:
        """
        Generate and return random text.

        Args:
            qty (int, optional): The number of text segments to generate.
                Defaults to 2.

        Returns:
            str: Randomly generated text.
        """
        return self.text.text(quantity=qty)

    def get_random_float(self, start: float, end: float) -> float:
        """
        Generate and return a random floating-point number within the specified
        range.

        Args:
            start (float): The lower bound of the range.
            end (float): The upper bound of the range.

        Returns:
            float: A random floating-point number.
        """
        return round(random.uniform(start, end), 2)

    def get_random_int(self, start: int, end: int) -> int:
        """
        Generate and return a random integer within the specified range.

        Args:
            start (int): The lower bound of the range.
            end (int): The upper bound of the range.

        Returns:
            int: A random integer.
        """
        return random.randint(start, end)

    def get_random_bool(self) -> bool:
        """
        Generate and return a random boolean value (True or False).

        Returns:
            bool: A randomly generated boolean value.
        """
        return random.choice((True, False))

    def get_random_datetime(self) -> datetime:
        """
        Generate and return a random datetime object.

        Returns:
            datetime: A randomly generated datetime object.
        """
        return self.date_time.datetime()

    def get_random_aware_datetime(self) -> datetime:
        """
        Generate and return a random timezone-aware datetime object.

        Returns:
            datetime: A randomly generated timezone-aware datetime object.
        """
        return pytz.UTC.localize(self.date_time.datetime())

    def get_random_file(self) -> str:
        """
        Generate and return a random file name.

        Returns:
            str: A randomly generated file name.
        """
        return self.file.file_name()

    def get_random_phone_number(self) -> int:
        """
        Generate and return a random 12-digit number that starts with '989'.

        Returns:
            int: A random 12-digit integer.
        """
        prefix = "989"
        random_digits = [
            random.randint(0, 9) for _ in range(5)
        ]  # Generate 9 random digits.
        random_phone_number = int(
            prefix + "".join(map(str, random_digits))
        )  # Concatenate the prefix and random digits.
        return random_phone_number

    def get_random_number(self) -> int:
        """
        Generate and return a random 12-digit number that starts with '015'.

        Returns:
            int: A random 12-digit integer.
        """
        prefix = "015"
        random_digits = [
            random.randint(0, 9) for _ in range(9)
        ]  # Generate 9 random digits.
        random_number = int(
            prefix + "".join(map(str, random_digits))
        )  # Concatenate the prefix and random digits.
        return random_number

    def get_random_transaction_number(self) -> str:
        """
        Generate and return a random transaction_number as a string.

        Returns:
            str: A randomly generated transaction_number.
        """
        return str(uuid.uuid4())

    def get_random_status(self):
        """
        Randomly selects and returns one of the following three strings: 'a', 'b', or 'c'.

        Returns:
        str: A randomly chosen string from 'SUCCESS', 'PENDING', 'FAILED'.
        """
        choices = ["SUCCESS", "PENDING", "FAILED"]
        return random.choice(choices)

    def get_random_string(self, length=10):
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(length))

    def get_random_brands(self) -> Brand:
        """
        Return a randomly chosen brand.

        Returns:
            Brand: A randomly selected brand.
        """
        brands = list(Brand.objects.all())
        return random.choice(brands)

    def get_random_categories(self) -> Category:
        """
        Return a randomly chosen category.

        Returns:
            Category: A randomly selected category.
        """
        categories = list(Category.objects.all())
        return random.choice(categories)

    def get_random_products(self) -> Brand:
        """
        Return a randomly chosen brand.

        Returns:
            Brand: A randomly selected brand.
        """
        products = list(Product.objects.all())
        return random.choice(products)

    def get_random_AttributeValue(self) -> AttributeValue:
        """
        Return a randomly chosen AttributeValue.

        Returns:
            AttributeValue: A randomly selected AttributeValue.
        """
        AttributeValues = list(AttributeValue.objects.all())
        return random.choice(AttributeValues)

    def get_random_user(self) -> User:
        """
        Return a randomly chosen user.

        Returns:
            user: A randomly selected user.
        """
        users = list(User.objects.all())
        return random.choice(users)

    def get_random_cart(self) -> Cart:
        """
        Return a randomly chosen cart.

        Returns:
            cart: A randomly selected cart.
        """
        carts = list(Cart.objects.all())
        return random.choice(carts)

    def get_random_order_address(self) -> OrderAddress:
        """
        Return a randomly chosen order_address.

        Returns:
            order_address: A randomly selected order_address.
        """
        order_address = list(OrderAddress.objects.all())
        return random.choice(order_address)

    def get_random_pack(self) -> Pack:
        """
        Return a randomly chosen pack.

        Returns:
            pack: A randomly selected pack.
        """
        pack = list(Pack.objects.all())
        return random.choice(pack)

    def get_random_corporate_profile(self) -> CorporateProfile:
        """
        Return a randomly chosen corporate_profile.

        Returns:
            corporate_profile: A randomly selected corporate_profile.
        """
        corporate_profile = list(CorporateProfile.objects.all())
        return random.choice(corporate_profile)

    def get_random_personal_profiles(self) -> PersonalProfile:
        """
        Return a randomly chosen personal_profiles.

        Returns:
            personal_profiles: A randomly selected personal_profiles.
        """
        personal_profiles = list(PersonalProfile.objects.all())
        return random.choice(personal_profiles)
