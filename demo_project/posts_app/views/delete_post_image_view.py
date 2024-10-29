from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View

from ..models import PostImage


class DeletePostImageView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, post_id: int, image_id: int):
        image = PostImage.objects.select_related("post").get(id=image_id)
        if image.post.user != request.user:
            return redirect("posts_app:all")

        image.delete()
        return redirect("posts_app:edit", id=post_id)
