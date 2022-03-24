from django.urls import path
from news.api.views import (
    posts_list,
    post_create,
    post_list,
    post_update,
    post_delete,
    comments_list,
    comment_create,
    comment_delete,
    upvote_post,
)


urlpatterns = [
    path("posts/", posts_list, name="posts-list"),
    path("posts/<int:pk>/", post_list, name="post-list"),
    path("post_create/", post_create, name="post-create"),
    path("post_update/<int:pk>/", post_update, name="post-update"),
    path("post_delete/<int:pk>/", post_delete, name="post-delete"),
    path("comments/", comments_list, name="comments-list"),
    path("comment_create/", comment_create, name="comment-create"),
    path("comment_delete/<int:pk>/", comment_delete, name="comment-delete"),
    path("upvote_post/<int:pk>/", upvote_post, name="upvote_post"),
]
