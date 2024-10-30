from django.contrib.auth import logout
from django.http import HttpRequest
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


@extend_schema(
    tags=["auth"],
    responses={
        204: None,
    },
)
class LogoutView(APIView):
    def post(self, request: HttpRequest):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
