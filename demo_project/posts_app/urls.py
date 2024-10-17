from django.urls import path

from .views.create_post_view import CreatePostView
from .views.post_view import PostsView


urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
]