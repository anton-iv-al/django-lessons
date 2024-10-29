from django.urls import path

from .views.all_media_view import AllMediaView
from .views.create_media_view import CreateMediaView
from media_app.api.views.media import MediaView as ApiMediaView




urlpatterns = [
    path('media/', AllMediaView.as_view(), name='all'),
    path('media/create/', CreateMediaView.as_view(), name='create'),

    path('api/media/', ApiMediaView.as_view({'post': 'create'}), name='api-media'),
]