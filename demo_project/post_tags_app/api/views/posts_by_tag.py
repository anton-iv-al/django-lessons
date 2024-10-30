from drf_spectacular.utils import extend_schema
from posts_app.api.serializers.posts import PostSerializer
from posts_app.models import Post
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet


@extend_schema(tags=["tag"])
class PostsByTagView(GenericViewSet, ListModelMixin):
    serializer_class = PostSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["created_at", "id"]
    ordering = ["-created_at", "id"]

    def get_queryset(self):
        tag_name = self.kwargs["tag"]
        return Post.objects.filter(tags__name=tag_name)
