from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from ..forms.registration_form import RegistrationForm

REGISTRATION_TEMPLATE = "registration.html"


class RegistrationView(View):
    def get(self, request: HttpRequest):
        form = RegistrationForm()
        context = {"reg_form": form}
        return render(request, REGISTRATION_TEMPLATE, context)

    def post(self, request: HttpRequest):
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            context = {"reg_form": form}
            return render(request, REGISTRATION_TEMPLATE, context)

        form.save()
        return redirect("/auth/login/")
