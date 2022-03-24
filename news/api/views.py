from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import Post, Comment
from news.api.serializers import PostSerializer, CommentSerializer


@api_view(["GET"])
def posts_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def post_create(request):
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def post_list(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        comments = post.comments.all()
        data = {
            "post": {
                "title": post.title,
                "link": post.link,
                "comments": list(comments.values("author", "content", "created_at")),
            }
        }
        response = Response(data)
    except Post.DoesNotExist:
        return Response(
            {"error": {"code": 404, "message": "Post not found!"}},
            status=status.HTTP_404_NOT_FOUND,
        )
    return response


@api_view(["PUT"])
def post_update(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(
            {"error": {"code": 404, "message": "Post not found!"}},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def post_delete(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(
            {"error": {"code": 404, "message": "Post not found!"}},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def comments_list(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def comment_create(request):
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def comment_delete(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(
            {"error": {"code": 404, "message": "Comment not found!"}},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def upvote_post(request, pk):
    upvote = request.POST.get("upvote")
    post = Post.objects.get(pk=pk)

    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save(upvote=upvote, author=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
