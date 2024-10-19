from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from posts_app import settings as app_settings

from ..models import Post

from ..forms.edit_post_form import EditPostForm


EDIT_POST_TEMPLATE = "edit_post.html"


class EditPostView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, id: int):
        post = Post.objects.prefetch_related("images").get(id=id)
        form = EditPostForm(instance=post)
        context = {
            "edit_post_form": form,
            "max_images": app_settings.MAX_IMAGES_FOR_POST,
        }
        return render(request, EDIT_POST_TEMPLATE, context)

    def post(self, request: HttpRequest, id: int):
        post = Post.objects.get(id=id)
        form = EditPostForm(request.POST, instance=post)
        if not form.is_valid():
            context = {"edit_post_form": form}
            return render(request, EDIT_POST_TEMPLATE, context)

        form.save()

        return redirect("posts_app:all")
