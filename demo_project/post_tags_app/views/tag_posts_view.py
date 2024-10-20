from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class TagPostsView(View):
    def get(self, request: HttpRequest, tag_name: str):
        return redirect(reverse("posts_app:all") + f"?tag={tag_name}")
