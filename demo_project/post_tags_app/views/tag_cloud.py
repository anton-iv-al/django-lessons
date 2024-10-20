from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from ..models import PostTag

TAGS_IN_CLOUD = 10


class TagCloudView(View):
    def get(self, request: HttpRequest):
        tags = PostTag.objects.order_by("-count", "name").all()[:TAGS_IN_CLOUD]
        return render(request, "tag_cloud.html", {"tags": tags})
