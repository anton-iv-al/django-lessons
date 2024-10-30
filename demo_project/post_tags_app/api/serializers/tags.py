from rest_framework import serializers

from ...models import PostTag


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ["id", "name", "count"]
        read_only_fields = ["id", "name", "count"]
