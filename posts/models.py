from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def get_recent_posts_liked(self):
        return self.posts.order_by("-id")[:3]


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, related_name="posts_authored")
    liked_by_users = models.ManyToManyField(
        User,
        through='Like',
        through_fields=('post', 'user'),
        related_name="posts_liked",
    )
    user = models.ForeignKey(User, related_name="posts")

    def get_recent_comments(self):
        return self.comments.all().order_by("-id")[:3]


class Comment(models.Model):
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name="comments")


class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes")
    user = models.ForeignKey(User, related_name="likes")

    class Meta:
        unique_together = ("post", "user",)
