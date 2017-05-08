from rest_framework.routers import SimpleRouter
from .views import PostsViewSet

router = SimpleRouter()
router.register('posts', PostsViewSet)

urlpatterns = router.urls
