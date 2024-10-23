from posts_app.api.serializers.posts import PostSerializer
from posts_app.models import Post
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet


class ApiPostsByTagView(GenericViewSet, ListModelMixin):
    serializer_class = PostSerializer
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        tag_name = self.kwargs["tag"]
        return Post.objects.filter(tags__name=tag_name)
