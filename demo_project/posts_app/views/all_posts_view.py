from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from post_tags_app.models import PostTag

from ..models import Post, PostImage


class PostsView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        if tag_name := request.GET.get("tag"):
            posts = Post.objects.filter(tags__name=tag_name)
        else:
            posts = Post.objects

        prefetch_images = Prefetch("images", queryset=PostImage.objects.order_by("id"))
        prefetch_tags = Prefetch("tags", queryset=PostTag.objects.order_by("name"))
        posts = (
            posts.prefetch_related(prefetch_images, prefetch_tags)
            .order_by("-created_at")
            .all()
        )

        context = {"posts": posts}
        return render(request, "all_posts.html", context)
