from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from likes_app.api.serializers.likes import LikeSerializer
from likes_app.models import Like


@extend_schema(tags=["like"])
class LikesView(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
):
    serializer_class = LikeSerializer
    queryset = Like.objects.prefetch_related("user").all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ["id"]
    filterset_fields = ["parent_likes_anchor"]
