from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from painless.models import TimestampMixin
from .post import Post

class Comment(TimestampMixin):
    """
    Model representing comments made on blog posts.
    """

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        help_text=_("The user who wrote the comment.")
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        help_text=_("The post on which the comment is made.")
    )

    content = models.TextField(
        help_text=_("The content of the comment.")
    )

    is_active = models.BooleanField(
        default=True,
        help_text=_("Whether the comment is visible and active.")
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-created']
        db_table = 'blog_comment'

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

    def deactivate(self):
        """
        Method to deactivate the comment (soft delete).
        """
        self.is_active = False
        self.save()
