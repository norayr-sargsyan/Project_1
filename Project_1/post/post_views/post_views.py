from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from post.models import Post, Comment, Likes
from post.post_serializers import PostSerializers, LikeSerializers, CommentSerializers


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Likes
    serializer_class = LikeSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LikeRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Likes
    serializer_class = LikeSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Comment
    serializer_class = CommentSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
