from django.contrib import admin
from blogs.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title',)
    search_filter = ('title',)
