from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from ..forms.edit_user_form import EditUserForm

USER_TEMPLATE = "user.html"


class UserView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        form = EditUserForm(instance=request.user)  # type: ignore
        context = {"edit_user_form": form}
        return render(request, USER_TEMPLATE, context)

    def post(self, request: HttpRequest):
        form = EditUserForm(request.POST, instance=request.user)  # type: ignore
        if not form.is_valid():
            context = {"edit_user_form": form}
            return render(request, USER_TEMPLATE, context)

        form.save()

        context = {"edit_user_form": form, "user": request.user}
        return render(request, USER_TEMPLATE, context)
