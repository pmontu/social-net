from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, LikeViewSet, PostsViewSet, UserViewSet

router = SimpleRouter()
router.register('users/(?P<user_id>\d+)/posts', PostsViewSet)
router.register('users/(?P<user_id>\d+)/posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('likes', LikeViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls
