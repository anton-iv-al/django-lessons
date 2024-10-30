from django.urls import path
from rest_framework.documentation import include
from rest_framework.routers import DefaultRouter

from .views.delete_post_image_view import DeletePostImageView
from .views.add_post_image_view import AddPostImageView
from .views.edit_post_view import EditPostView
from .views.create_post_view import CreatePostView
from .views.all_posts_view import PostsView
from .api.views.posts import PostsView as ApiPostsView


post_api_router = DefaultRouter()
post_api_router.register("post", ApiPostsView)

urlpatterns = [
    path('post/', PostsView.as_view(), name='all'),
    path('post/create/', CreatePostView.as_view(), name='create'),
    path('post/<int:id>/', EditPostView.as_view(), name='edit'),
    path('post/<int:post_id>/image/add', AddPostImageView.as_view(), name='image_add'),
    path('post/<int:post_id>/image/<int:image_id>/delete', DeletePostImageView.as_view(), name='image_delete'),

    path('api/', include(post_api_router.urls), name="api-posts"),
]