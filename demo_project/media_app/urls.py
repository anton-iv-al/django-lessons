from django.urls import path

from .views.all_media_view import AllMediaView

from .views.create_media_view import CreateMediaView




urlpatterns = [
    path('media/', AllMediaView.as_view(), name='all'),
    path('media/create/', CreateMediaView.as_view(), name='create'),
]