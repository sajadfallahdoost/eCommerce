from django.contrib import admin


from blog.models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'category', 'published_date', 'created', 'modified')
    search_fields = ('title', 'slug', 'content')
    list_filter = ('status', 'author', 'category', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'modified', 'published_date')
    date_hierarchy = 'published_date'
    ordering = ('-published_date', '-created')
