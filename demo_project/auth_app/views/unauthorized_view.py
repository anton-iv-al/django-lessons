from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class UnathorizedView(View):
    def get(self, request: HttpRequest):
        return render(request, "unauthorized.html")
