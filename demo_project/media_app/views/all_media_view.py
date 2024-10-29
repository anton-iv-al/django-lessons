from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from ..models import Media


class AllMediaView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        media_items = Media.objects.prefetch_related("user").all()
        context = {"media_items": media_items}
        return render(request, "all_media.html", context)
