from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from ..forms.edit_user_profile_form import EditUserProfileForm

from ..forms.edit_user_form import EditUserForm

USER_TEMPLATE = "user.html"


class UserView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        user_form = EditUserForm(
            instance=request.user,  # type: ignore
            prefix="user",
        )
        profile_form = EditUserProfileForm(
            instance=request.user.profile,  # type: ignore
            prefix="profile",
        )
        context = {"edit_user_form": user_form, "edit_profile_form": profile_form}
        return render(request, USER_TEMPLATE, context)

    def post(self, request: HttpRequest):
        user_form = EditUserForm(
            request.POST,
            instance=request.user,  # type: ignore
            prefix="user",
        )
        profile_form = EditUserProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile,  # type: ignore
            prefix="profile",
        )

        user_form.is_valid()
        profile_form.is_valid()
        if user_form.errors or profile_form.errors:
            context = {"edit_user_form": user_form, "edit_profile_form": profile_form}
            return render(request, USER_TEMPLATE, context)

        with transaction.atomic():
            user_form.save()
            profile_form.save()

        context = {"edit_user_form": user_form, "edit_profile_form": profile_form}
        return render(request, USER_TEMPLATE, context)
