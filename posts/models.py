from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User)
    liked_by_users = models.ManyToManyField(
        User,
        through='Like',
        through_fields=('post', 'user'),
        related_name="posts_liked"
    )


class Comment(models.Model):
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name="comments")


class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes")
    user = models.ForeignKey(User, related_name="likes")

    class Meta:
        unique_together = ("post", "user",)

