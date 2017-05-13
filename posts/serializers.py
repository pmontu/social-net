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


class HyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def get_url(self, obj, view_name, request, format):
        """
        Given an object, return the URL that hyperlinks to the object.

        May raise a `NoReverseMatch` if the `view_name` and `lookup_field`
        attributes are not configured to correctly match the URL conf.
        """
        # Unsaved objects will not yet have a valid URL.
        if hasattr(obj, 'pk') and obj.pk in (None, ''):
            return None

        lookup_value = getattr(obj, self.lookup_field)
        kwargs = {self.lookup_url_kwarg: lookup_value}
        kwargs["user_id"] = self.context["view"].kwargs["pk"]
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)


class UserSerializer(serializers.ModelSerializer):
    recent_likes = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        source="get_recent_posts_liked",
        view_name="post-detail",
        lookup_field="pk",
        lookup_url_kwarg="pk"
     )

    class Meta:
        model = User
        fields = ("username", "recent_likes", )
