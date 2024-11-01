from django.contrib.auth import login
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from auth_app.api.serializers.users import UserSerializer, UserWithPasswordSerializer


@extend_schema(tags=["auth/user"])
class RegisterView(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
):
    serializer_class = UserWithPasswordSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = [OrderingFilter]
    ordering_fields = ["date_joined", "id"]
    ordering = ["-date_joined"]

    def get_serializer_class(self):
        if self.action == "create":
            return UserWithPasswordSerializer
        else:
            return UserSerializer

    def perform_create(self, serializer: UserWithPasswordSerializer):
        user = serializer.save()
        login(self.request, user)
