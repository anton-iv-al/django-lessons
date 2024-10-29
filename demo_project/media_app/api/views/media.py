import magic
from django.core.files.uploadedfile import UploadedFile
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from media_app.api.serializers.media import MediaSerializer
from media_app.models import Media, MediaType


class MediaView(GenericViewSet, CreateModelMixin):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        file: UploadedFile | None = serializer.validated_data.get("file")
        if file is not None:
            file_type = magic.from_buffer(file.read(), mime=True)
            if "image" in file_type:
                media_type = MediaType.IMAGE.value
            else:
                raise ValidationError("Unavailable file type.")

        serializer.save(media_type=media_type)
