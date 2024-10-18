from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View


class LogoutView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(request.GET.get("next", "main_app:index"))
