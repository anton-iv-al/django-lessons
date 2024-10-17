from django.urls import path
from .views.registration_view import RegistrationView
from .views.login_view import LoginView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
]