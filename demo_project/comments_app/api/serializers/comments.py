from rest_framework import serializers

from comments_app.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "created_at",
            "parent_comments_anchor",
            "text",
            "hidden_user",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
        ]

    hidden_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
