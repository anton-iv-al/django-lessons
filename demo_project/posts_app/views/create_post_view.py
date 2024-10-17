from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from ..forms.create_post_form import CreatePostForm


class CreatePostView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        form = CreatePostForm()
        context = {"create_post_form": form}
        return render(request, "create_post.html", context)

    def post(self, request: HttpRequest):
        form = CreatePostForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {"create_post_form": form}
            return render(request, "create_post.html", context)

        form.save()
        return redirect("posts_app:posts")
