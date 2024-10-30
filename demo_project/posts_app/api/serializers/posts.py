from rest_framework import serializers

from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "user"]

    post_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
