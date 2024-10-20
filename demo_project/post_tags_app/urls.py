from django.urls import path

from .views.tag_cloud import TagCloudView
from .views.tag_posts_view import TagPostsView

urlpatterns = [
    path("", TagCloudView.as_view(), name="cloud"),
    path("<str:tag_name>/", TagPostsView.as_view(), name="tag"),
]
