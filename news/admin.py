from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "author", "upvote", "created_at")
    list_filter = ("title", "author", "created_at")
    search_fields = ("title", "author")
    raw_id_fields = ("author",)
    date_hierarchy = "created_at"
    ordering = ("upvote", "created_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "post", "created_at")
    list_filter = ("created_at",)
    search_fields = (
        "author",
        "content",
    )
