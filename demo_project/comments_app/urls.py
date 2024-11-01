from django.urls import path
from rest_framework.documentation import include
from rest_framework.routers import DefaultRouter

from comments_app.api.views.comments import CommentsView



comments_api_router = DefaultRouter()
comments_api_router.register("comment", CommentsView)

urlpatterns = [
    path('api/', include(comments_api_router.urls), name="api-comments"),
]