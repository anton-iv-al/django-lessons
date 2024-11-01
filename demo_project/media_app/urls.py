from django.urls import path
from rest_framework.documentation import include
from rest_framework.routers import DefaultRouter

from .views.all_media_view import AllMediaView
from .views.create_media_view import CreateMediaView
from media_app.api.views.media import MediaView as ApiMediaView


media_api_router = DefaultRouter()
media_api_router.register("media", ApiMediaView)

urlpatterns = [
    path('media/', AllMediaView.as_view(), name='all'),
    path('media/create/', CreateMediaView.as_view(), name='create'),

    path('api/', include(media_api_router.urls), name="api-media"),
]