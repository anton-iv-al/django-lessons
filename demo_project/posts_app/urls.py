from django.urls import path

from .views.delete_post_image_view import DeletePostImageView
from .views.add_post_image_view import AddPostImageView
from .views.edit_post_view import EditPostView
from .views.create_post_view import CreatePostView
from .views.all_posts_view import PostsView


urlpatterns = [
    path('', PostsView.as_view(), name='all'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('<int:id>/', EditPostView.as_view(), name='edit'),
    path('<int:post_id>/image/add', AddPostImageView.as_view(), name='image_add'),
    path('<int:post_id>/image/<int:image_id>/delete', DeletePostImageView.as_view(), name='image_delete'),
]