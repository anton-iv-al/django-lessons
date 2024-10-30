from typing import cast

from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.api.serializers.login import LoginSerializer


@extend_schema(
    tags=["auth"],
    request=LoginSerializer,
    responses={
        204: None,
    },
)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = cast(dict, serializer.validated_data)

        user = authenticate(
            request,
            username=request_data["username"],
            password=request_data["password"],
        )
        if user is None:
            return Response(
                {"detail": "Wrong credentials."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        login(request, user)
        return Response(status=status.HTTP_204_NO_CONTENT)
