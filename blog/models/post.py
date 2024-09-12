from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from painless.models import TitleSlugMixin, TimestampMixin, PictureOperationAbstract
from blog.models.category import Category

class Post(TimestampMixin, TitleSlugMixin, PictureOperationAbstract):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts',
        help_text=_("The user who wrote the post.")
    )

    image = models.ImageField(
        upload_to='posts/%Y/%m/%d/',
        null=True,
        blank=True,
        help_text=_("The main image associated with the post.")
    )

    content = models.TextField(
        help_text=_("The main body content of the post.")
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        help_text=_("The publication status of the post.")
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        help_text=_("The category to which the post belongs.")
    )

    published_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_("The date and time when the post was published.")
    )

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-published_date', '-created']
        db_table = 'blog_post'

    def __str__(self):
        return self.title

    def publish(self):
        """Method to publish the post."""
        self.status = 'published'
        self.published_date = models.DateTimeField.now()
        self.save()
