from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

@admin.register(Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "created_at", "views_count")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "content")
    readonly_fields = ("views_count", "created_at", "updated_at")
