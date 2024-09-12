from django.contrib import admin
from blog.models.comment import Comment

class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for managing comments.
    """
    list_display = ('author', 'post', 'content', 'is_active', 'created')
    list_filter = ('is_active', 'created', 'post__category')
    search_fields = ('author__username', 'author__email', 'content', 'post__title')
    actions = ['deactivate_comments', 'activate_comments']
    list_editable = ('is_active',)
    ordering = ('-created',)

    def deactivate_comments(self, request, queryset):
        """
        Custom admin action to deactivate selected comments.
        """
        queryset.update(is_active=False)
        self.message_user(request, "Selected comments have been deactivated.")
    deactivate_comments.short_description = "Deactivate selected comments"

    def activate_comments(self, request, queryset):
        """
        Custom admin action to activate selected comments.
        """
        queryset.update(is_active=True)
        self.message_user(request, "Selected comments have been activated.")
    activate_comments.short_description = "Activate selected comments"

# Register the Comment model with the custom admin class
admin.site.register(Comment, CommentAdmin)
