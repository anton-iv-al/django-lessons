from rest_framework import serializers

from media_app.models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["file", "media_type", "user", "hidden_user"]
        read_only_fields = ["media_type", "user"]

    hidden_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
