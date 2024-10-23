from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ...models import PostTag
from ..serializers.tags import PostTagSerializer


class ApiTagsView(GenericViewSet, ListModelMixin):
    serializer_class = PostTagSerializer
    queryset = PostTag.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ["count", "name"]
    ordering = ["-count", "name"]
