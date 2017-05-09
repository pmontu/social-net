from rest_framework.routers import SimpleRouter
from .views import (
    PostsViewSet, CommentViewSet, LikeViewSet,
    UserViewSet
)

router = SimpleRouter()
router.register('posts', PostsViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls
