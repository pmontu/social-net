from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import (PostSerializer,
    CommentSerializer, LikeSerializer, UserSerializer
)
from .models import Post, Comment, Like
from .permissions import IsOwnerOrReadOnly, AdminOnlyDelete
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User


class PostsViewSet(ModelViewSet):
        serializer_class = PostSerializer
        queryset = Post.objects.filter()
        permission_classes = (IsOwnerOrReadOnly,)


class CommentViewSet(
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
        serializer_class = CommentSerializer
        queryset = Comment.objects.filter()
        permission_classes = (AllowAny, AdminOnlyDelete,)


class LikeViewSet(
                     mixins.CreateModelMixin,
                     GenericViewSet):
        serializer_class = LikeSerializer
        queryset = Like.objects.filter()
        permission_classes = (IsAuthenticated,)

class UserViewSet(
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
        serializer_class = UserSerializer
        queryset = User.objects.filter()
        permission_classes = (IsAuthenticated,)

