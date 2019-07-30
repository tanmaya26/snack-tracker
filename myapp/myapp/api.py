from rest_framework import routers
from snacktracker import views

router = routers.DefaultRouter()
router.register(r'requests', views.ListRequests)
router.register(r'tags', views.ListTags)
router.register(r'likes', views.ListLikes)
router.register(r'snacks', views.ListSnacks)
router.register(r'images', views.ListImages)
router.register(r'dislikes', views.ListDisikes)
router.register(r'users', views.ListUsers)


