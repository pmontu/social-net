from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
from .permissions import IsOwnerOrReadOnly


class PostsViewSet(ModelViewSet):
        serializer_class = PostSerializer
        queryset = Post.objects.filter()
        permission_classes = (IsOwnerOrReadOnly,)

