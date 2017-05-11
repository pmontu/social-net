from rest_framework import serializers

from .models import Comment, Like, Post, User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("body", "post", "id")
        read_only_fields = ("post",)

    def create(self, validated_data):
        post_id = self.context["view"].kwargs["post_id"]
        validated_data["post"] = Post.objects.get(id=post_id)
        comment = Comment.objects.create(**validated_data)
        return comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    recent_comments = CommentSerializer(
         many=True,
         read_only=True,
         source="get_recent_comments"
     )
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("title", "body", "author", "id", "recent_comments", "likes")

    def create(self, validated_data):
        user_id = self.context["view"].kwargs["user_id"]
        validated_data["user"] = User.objects.get(id=user_id)
        post = Post.objects.create(**validated_data)
        return post

    def get_likes(self, obj):
        return obj.likes.count()


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True)

    class Meta:
        model = Like
        fields = ("user", "post", )


class ContentSerializer(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.PrimaryKeyRelatedField(read_only=True)


class UserSerializer(serializers.ModelSerializer):
    recent_likes = ContentSerializer(
        many=True,
        read_only=True,
        source="get_recent_posts_liked"
     )

    class Meta:
        model = User
        fields = ("username", "recent_likes", )
