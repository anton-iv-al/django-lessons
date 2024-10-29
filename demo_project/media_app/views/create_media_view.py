import magic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import UploadedFile
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from rest_framework.request import HttpRequest

from media_app.models import Media, MediaType

from ..forms.create_media_form import CreateMediaForm


class CreateMediaView(LoginRequiredMixin, View):
    template = "create_media.html"

    def get(self, request: HttpRequest):
        form = CreateMediaForm()
        return render(request, self.template, {"media_form": form})

    def post(self, request: HttpRequest):
        form = CreateMediaForm(request.POST, request.FILES)

        form.is_valid()

        file: UploadedFile | None = form.cleaned_data.get("file")
        if file is not None:
            file_type = magic.from_buffer(file.read(), mime=True)
            if "image" in file_type:
                media_type = MediaType.IMAGE.value
            else:
                form.add_error("file", "Unavailable file type.")

        if form.errors:
            return render(request, self.template, {"media_form": form})

        media: Media = form.save(commit=False)
        media.user = request.user
        media.media_type = media_type
        media.save()
        return redirect(reverse("media_app:all"))
