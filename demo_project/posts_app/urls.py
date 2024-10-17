from django.urls import path

from .views.create_post_view import CreatePostView
from .views.post_view import PostsView


urlpatterns = [
    path('', PostsView.as_view(), name='all'),
    path('create/', CreatePostView.as_view(), name='create'),
]