from django.urls import path

from .api.views.posts_by_tag import ApiPostsByTagView

from .api.views.tags import ApiTagsView

from .views.tag_cloud import TagCloudView
from .views.tag_posts_view import TagPostsView

urlpatterns = [
    path("", TagCloudView.as_view(), name="cloud"),
    path("<str:tag_name>/", TagPostsView.as_view(), name="tag"),

    path('api', ApiTagsView.as_view({'get': 'list'}), name='api-tags'),
    path('api/<str:tag>', ApiPostsByTagView.as_view({'get': 'list'}), name='api-posts-by-tag'),
]
