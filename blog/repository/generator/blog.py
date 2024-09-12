import random
from typing import List
from faker import Faker
from tqdm import tqdm
from django.contrib.auth.models import User
from blog.models.category import Category
from blog.models.post import Post
from blog.models.comment import Comment
from painless.repository.generator import BaseDataGenerator

fake = Faker()

class BlogDataGenerator(BaseDataGenerator):
    """
    A class responsible for generating fake data for blog-related tables.
    Inherits from BaseDataGenerator for data generation utilities.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BlogDataGenerator.
        """
        super().__init__(*args, **kwargs)
        self.used_users = set()

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

    def create_categories(self, total: int = 10, disable_progress_bar: bool = False) -> List[Category]:
        """
        Generate and create fake categories.

        Args:
            total (int): The total number of categories to create. Default is 10.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Category]: A list of created categories.
        """
        categories = [
            Category(name=fake.word()[:50])
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return Category.objects.bulk_create(categories)

    def create_posts(self, total: int = 50, disable_progress_bar: bool = False) -> List[Post]:
        """
        Generate and create fake blog posts.

        Args:
            total (int): The total number of posts to create. Default is 50.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Post]: A list of created posts.
        """
        users = list(User.objects.all())
        categories = list(Category.objects.all())

        posts = [
            Post(
                title=fake.sentence()[:255],
                content=fake.paragraph(nb_sentences=10),
                author=random.choice(users),
                category=random.choice(categories) if categories else None,
                created_at=fake.date_time_this_year(),
                updated_at=fake.date_time_this_year(),
                status=random.choice(['draft', 'published'])
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return Post.objects.bulk_create(posts)

    def create_comments(self, total: int = 100, disable_progress_bar: bool = False) -> List[Comment]:
        """
        Generate and create fake comments.

        Args:
            total (int): The total number of comments to create. Default is 100.
            disable_progress_bar (bool): Disable the tqdm progress bar. Default is False.

        Returns:
            List[Comment]: A list of created comments.
        """
        users = list(User.objects.all())
        posts = list(Post.objects.all())

        comments = [
            Comment(
                post=random.choice(posts),
                author=random.choice(users),
                content=fake.sentence(),
                created_at=fake.date_time_this_year(),
                updated_at=fake.date_time_this_year(),
            )
            for _ in tqdm(range(total), disable=disable_progress_bar)
        ]
        return Comment.objects.bulk_create(comments)

    def generate_all_data(self, users_total: int = 50, categories_total: int = 10, posts_total: int = 50, comments_total: int = 100):
        """
        Helper function to generate all data: users, categories, posts, and comments.
        """
        print("Generating Users...")
        self.create_users(total=users_total)
        
        print("Generating Categories...")
        self.create_categories(total=categories_total)
        
        print("Generating Posts...")
        self.create_posts(total=posts_total)
        
        print("Generating Comments...")
        self.create_comments(total=comments_total)

