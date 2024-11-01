from django.http import HttpRequest
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.api.serializers.users import UserSerializer


@extend_schema(
    tags=["auth/user"],
    responses={
        200: UserSerializer,
    },
)
class UserCurrentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest):
        serializer = UserSerializer(request.user)
        return Response(data=serializer.data)
