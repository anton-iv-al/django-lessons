from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import NON_FIELD_ERRORS
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from ..models import PostImage

from ..forms.add_post_image_form import AddPostImageForm

from posts_app import settings as app_settings


ADD_POST_IMAGE_TEMPLATE = "add_post_image.html"


class AddPostImageView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, post_id: int):
        form = AddPostImageForm()
        context = {"add_image_form": form, "post_id": post_id}
        return render(request, ADD_POST_IMAGE_TEMPLATE, context)

    def post(self, request: HttpRequest, post_id: int):
        images_count = PostImage.objects.filter(post_id=post_id).count()

        form = AddPostImageForm(request.POST, request.FILES)

        form.is_valid()
        if images_count >= app_settings.MAX_IMAGES_FOR_POST:
            form.add_error(NON_FIELD_ERRORS, "Image limit for this post is reached.")
        if form.errors:
            context = {"add_image_form": form, "post_id": post_id}
            return render(request, ADD_POST_IMAGE_TEMPLATE, context)

        post_image: PostImage = form.save(commit=False)
        post_image.post_id = post_id  # type: ignore
        post_image.save()

        return redirect("posts_app:edit", id=post_id)
