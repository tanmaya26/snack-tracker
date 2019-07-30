from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UploadImage, AddUser, SnackDetail, SnackList, TagList, TagDetail, LikeList, LikeDetail, \
    DislikeDetail, DislikeList, RequestDetail, RequestList, UserList, UserDetail, RequestSnack

urlpatterns = [
    re_path(r'^upload/$', UploadImage.as_view(), name='upload'),
    re_path(r'^user/$', AddUser.as_view(), name='add-user'),
    re_path(r'^request/$', RequestSnack.as_view(), name='request'),
    path('snacks/', SnackList.as_view()),
    path('snacks/<int:pk>/', SnackDetail.as_view()),
    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagDetail.as_view()),
    path('likes/', LikeList.as_view()),
    path('likes/<int:pk>/', LikeDetail.as_view()),
    path('dislikes/', DislikeList.as_view()),
    path('dislikes/<int:pk>/', DislikeDetail.as_view()),
    path('requests/', RequestList.as_view()),
    path('requests/<int:pk>/', RequestDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
