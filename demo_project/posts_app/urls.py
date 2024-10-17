from django.urls import path

from .views.post_view import PostView


urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
]