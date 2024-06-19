import random
from typing import List, Set
from faker import Faker
from tqdm import tqdm
from django.contrib.auth.models import User
from account.models import Address, CorporateProfile, PersonalProfile
from painless.repository.generator import BaseDataGenerator

fake = Faker()


class AccountDataGenerator(BaseDataGenerator):
    """
    A class responsible for generating fake data for account-related tables.
    Inherits from BaseDataGenerator for data generation utilities.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the AccountDataGenerator.

        Attributes:
            used_national_codes (Set[str]): A set of used national codes.
            used_register_numbers (Set[str]): A set of used register numbers.
            used_phone_numbers (Set[str]): A set of used phone numbers.
            used_users (Set[User]): A set of used users to ensure uniqueness.
        """
        super().__init__(*args, **kwargs)
        self.used_national_codes: Set[str] = set()
        self.used_register_numbers: Set[str] = set()
        self.used_phone_numbers: Set[str] = set()
        self.used_users: Set[User] = set()

    def get_random_user(self) -> User:
        """
        Return a randomly chosen user that has not been used yet.

        Returns:
            User: A randomly selected user.
        """
        users = list(User.objects.exclude(id__in=[user.id for user in self.used_users]))
        if not users:
            raise ValueError("No more unique users available")
        user = random.choice(users)
        self.used_users.add(user)
        return user

    def create_users(
        self, total: int = 200, batch_size: int = 10, disable_progress_bar: bool = False
    ) -> List[User]:
        """
        Generate and create fake user.

        Args:
            total (int): The total number of user to create. Default is 200.
            batch_size (int): The number of user to create per batch. Default is 10.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Pack]: A list of created user.
        """

        users = [
            User(
                username=fake.user_name() + str(_),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password=fake.password()
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return User.objects.bulk_create(users)

    def create_addresses(self, total: int = 100, disable_progress_bar: bool = False) -> List[Address]:
        """
        Generate and create fake addresses.

        Args:
            total (int): The total number of addresses to create. Default is 100.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Address]: A list of created addresses.
        """
        corporate_profiles = list(CorporateProfile.objects.all())
        personal_profiles = list(PersonalProfile.objects.all())

        addresses = [
            Address(
                address_line_1=fake.street_address()[:255],
                address_line_2=fake.secondary_address()[:255],
                city=fake.city()[:50],
                state=fake.state()[:50],
                zip_code=fake.postcode()[:10],
                country=fake.country()[:50],
                corporate_profile=random.choice(corporate_profiles) if corporate_profiles else None,
                personal_profile=random.choice(personal_profiles) if personal_profiles else None,
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return Address.objects.bulk_create(addresses)

    def create_corporate_profiles(self, total: int = 50, disable_progress_bar: bool = False) -> List[CorporateProfile]:
        """
        Generate and create fake corporate profiles.

        Args:
            total (int): The total number of corporate profiles to create. Default is 50.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[CorporateProfile]: A list of created corporate profiles.
        """
        corporate_profiles = [
            CorporateProfile(
                user=self.get_random_user(),
                name=fake.company()[:100],
                national_code=self.get_random_number(),
                register_number=self.get_random_number(),
                economical_code=self.get_random_number(),
                phone=self.get_random_phone_number()
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return CorporateProfile.objects.bulk_create(corporate_profiles)

    def create_personal_profiles(self, total: int = 50, disable_progress_bar: bool = False) -> List[PersonalProfile]:
        """
        Generate and create fake personal profiles.

        Args:
            total (int): The total number of personal profiles to create. Default is 50.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[PersonalProfile]: A list of created personal profiles.
        """
        personal_profiles = [
            PersonalProfile(
                user=self.get_random_user(),
                first_name=fake.first_name()[:1024],
                last_name=fake.last_name()[:1024],
                national_code=self.get_random_number(),
                gender=random.choice(['male', 'female']),
                phone=self.get_random_phone_number(),
                birth_date=fake.date_of_birth(),
                job=fake.job()[:1024]
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return PersonalProfile.objects.bulk_create(personal_profiles)
