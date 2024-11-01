from auth_app.api.serializers.users import UserSerializer
from rest_framework import serializers

from likes_app.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            "id",
            "user",
            "created_at",
            "parent_likes_anchor",
            "like_user",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
        ]

    like_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )

    user = UserSerializer(read_only=True)
