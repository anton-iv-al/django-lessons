from django.urls import path

from .api.views.posts_by_tag import PostsByTagView as ApiPostsByTagView

from .api.views.tags import TagsView as ApiTagsView

from .views.tag_cloud import TagCloudView
from .views.tag_posts_view import TagPostsView

urlpatterns = [
    path("tag/", TagCloudView.as_view(), name="cloud"),
    path("tag/<str:tag_name>/", TagPostsView.as_view(), name="tag"),

    path('api/tag', ApiTagsView.as_view({'get': 'list'}), name='api-tags'),
    path('api/tag/<str:tag>', ApiPostsByTagView.as_view({'get': 'list'}), name='api-posts-by-tag'),
]
