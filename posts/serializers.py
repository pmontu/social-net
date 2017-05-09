from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("body", "post", "id")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True)
    comments = CommentSerializer(many=True,
                                 read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("title", "body", "author", "id", "comments", "likes")

    def get_likes(self, obj):
        return obj.likes.count()




class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True)

    class Meta:
        model = Like
        fields = ("user", "post", )


class UserSerializer(serializers.ModelSerializer):
    # likes = LikeSerializer(many=True, read_only=True)
    # posts_liked = serializers.SerializerMethodField()
    posts_liked = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )

    class Meta:
        model = User
        fields = ("username", "posts_liked", )

    # def get_posts_liked(self, obj):
    #     serializer = PostSerializer(
    #         Post.objects.filter(likes__user=obj), many=True)
    #     return serializer.data
