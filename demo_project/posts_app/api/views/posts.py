from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from ...models import Post
from ..serializers.posts import PostSerializer


@extend_schema(tags=["post"])
class PostsView(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "id"]
    ordering = ["-created_at", "id"]
