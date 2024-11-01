from rest_framework import serializers

from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "created_at",
            "title",
            "text",
            "comments_anchor",
            "likes_anchor",
            "post_user",
            "images",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
            "comments_anchor",
            "likes_anchor",
        ]

    post_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
