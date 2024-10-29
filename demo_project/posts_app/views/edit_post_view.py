from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from demo_project import settings

from ..forms.edit_post_form import EditPostForm
from ..models import Post, PostImage

EDIT_POST_TEMPLATE = "edit_post.html"


class EditPostView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, id: int):
        prefetch_images = Prefetch(
            "images", queryset=PostImage.objects.select_related("image_data")
        )
        post = Post.objects.prefetch_related(prefetch_images).get(id=id)
        if post.user != request.user:
            return redirect("posts_app:all")

        form = EditPostForm(instance=post)
        context = {
            "edit_post_form": form,
            "max_images": settings.MAX_IMAGES_FOR_POST,
        }
        return render(request, EDIT_POST_TEMPLATE, context)

    def post(self, request: HttpRequest, id: int):
        post = Post.objects.get(id=id)
        if post.user != request.user:
            raise Exception("Not allowed.")

        form = EditPostForm(request.POST, instance=post)
        if not form.is_valid():
            context = {"edit_post_form": form}
            return render(request, EDIT_POST_TEMPLATE, context)

        form.save()

        return redirect("posts_app:all")
