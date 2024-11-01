from django.urls import path
from rest_framework.documentation import include
from rest_framework.routers import DefaultRouter

from likes_app.api.views.likes import LikesView


likes_api_router = DefaultRouter()
likes_api_router.register("like", LikesView)

urlpatterns = [
    path('api/', include(likes_api_router.urls), name="api-likes"),
]