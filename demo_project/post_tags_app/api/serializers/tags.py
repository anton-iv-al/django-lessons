from rest_framework import serializers

from ...models import PostTag


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ["name", "count"]
