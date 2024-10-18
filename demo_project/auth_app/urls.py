from django.urls import path

from .views.unauthorized_view import UnathorizedView
from .views.user_view import UserView
from .views.registration_view import RegistrationView
from .views.login_view import LoginView

urlpatterns = [
    path('unauthorized/', UnathorizedView.as_view(), name='unauthorized'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
]