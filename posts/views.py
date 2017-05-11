from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Comment, Like, Post, User
from .permissions import AdminOnlyDelete, IsOwnerOrReadOnly
from .serializers import (CommentSerializer, LikeSerializer, PostSerializer,
                          UserSerializer)


class PostsViewSet(ModelViewSet):
        serializer_class = PostSerializer
        queryset = Post.objects.filter()
        permission_classes = (IsOwnerOrReadOnly,)
        filter_fields = ("author",)

        def filter_queryset(self, queryset):
            queryset = super(PostsViewSet, self).filter_queryset(queryset)
            return queryset.filter(user__id=self.kwargs["user_id"])


class CommentViewSet(
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
        serializer_class = CommentSerializer
        queryset = Comment.objects.filter()
        permission_classes = (AllowAny, AdminOnlyDelete,)

        def filter_queryset(self, queryset):
            queryset = super(CommentViewSet, self).filter_queryset(queryset)
            return queryset.filter(post__user__id=self.kwargs["user_id"], post__id=self.kwargs["post_id"])


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
