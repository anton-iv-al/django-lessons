from django.contrib.auth import authenticate, login
from django.core.exceptions import NON_FIELD_ERRORS
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from ..forms.login_form import LoginForm


LOGIN_TEMPLATE = "login.html"


class LoginView(View):
    def get(self, request: HttpRequest):
        form = LoginForm()
        context = {"login_form": form}
        return render(request, LOGIN_TEMPLATE, context)

    def post(self, request: HttpRequest):
        form = LoginForm(request.POST)

        if not form.is_valid():
            context = {"login_form": form}
            return render(request, LOGIN_TEMPLATE, context)

        user = authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is None:
            form.add_error(NON_FIELD_ERRORS, "Unable to authenticate.")
            context = {"login_form": form}
            return render(request, LOGIN_TEMPLATE, context)

        login(request, user)
        return redirect(request.GET.get("next", "/"))
