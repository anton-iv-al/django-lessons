from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ..models import Post


class PostView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.order_by("-created_at").all()
        context = {"posts": posts}
        return render(request, "posts.html", context)
