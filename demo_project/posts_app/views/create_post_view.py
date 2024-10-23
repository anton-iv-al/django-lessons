from typing import cast

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from demo_project import settings

from ..forms.create_post_form import CreatePostForm, PostImageFormSet
from ..models import Post


class CreatePostView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        post_form = CreatePostForm()
        image_formset = PostImageFormSet()

        context = {"post_form": post_form, "image_formset": image_formset}
        return render(request, "create_post.html", context)

    def post(self, request: HttpRequest):
        post_form = CreatePostForm(request.POST, request.FILES)
        image_formset = PostImageFormSet(request.POST, request.FILES)

        if not post_form.is_valid() or not image_formset.is_valid():
            context = {"post_form": post_form, "image_formset": image_formset}
            return render(request, "create_post.html", context)

        with transaction.atomic():
            post: Post = post_form.save(commit=False)
            post.username = cast(User, request.user).username
            post.save()

            image_formset.instance = post
            images = image_formset.save(commit=False)
            if len(images) > settings.MAX_IMAGES_FOR_POST:
                raise Exception("MAX_IMAGES_FOR_POST exceeded")
            image_formset.save()

        return redirect("posts_app:all")
