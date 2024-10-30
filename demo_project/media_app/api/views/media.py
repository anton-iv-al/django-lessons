import magic
from django.core.files.uploadedfile import UploadedFile
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from media_app.api.serializers.media import MediaSerializer
from media_app.models import Media, MediaType


@extend_schema(tags=["media"])
class MediaView(GenericViewSet, CreateModelMixin):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

    def perform_create(self, serializer):
        file: UploadedFile | None = serializer.validated_data.get("file")
        if file is not None:
            file_type = magic.from_buffer(file.read(), mime=True)
            if "image" in file_type:
                media_type = MediaType.IMAGE.value
            else:
                raise ValidationError("Unavailable file type.")

        serializer.save(media_type=media_type)