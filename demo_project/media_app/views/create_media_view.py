from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from rest_framework.request import HttpRequest

from media_app.models import Media

from ..forms.create_media_form import CreateMediaForm


class CreateMediaView(LoginRequiredMixin, View):
    template = "create_media.html"

    def get(self, request: HttpRequest):
        form = CreateMediaForm()
        return render(request, self.template, {"media_form": form})

    def post(self, request: HttpRequest):
        form = CreateMediaForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, self.template, {"media_form": form})

        media: Media = form.save(commit=False)
        media.user = request.user
        media.save()
        return redirect(reverse("media_app:all"))
