from rest_framework.filters import OrderingFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ...models import Post
from ..serializers.posts import PostSerializer


class ApiPostsView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "id"]
    ordering = ["-created_at", "id"]
