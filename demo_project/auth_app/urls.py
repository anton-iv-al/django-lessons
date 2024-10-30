from django.urls import path

from .views.logout_view import LogoutView
from .views.unauthorized_view import UnathorizedView
from .views.user_view import UserView
from .views.registration_view import RegistrationView
from .views.login_view import LoginView
from .api.views.login import LoginView as ApiLoginView
from .api.views.logout import LogoutView as ApiLogoutView

urlpatterns = [
    path('auth/unauthorized/', UnathorizedView.as_view(), name='unauthorized'),
    path('auth/registration/', RegistrationView.as_view(), name='registration'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/user/', UserView.as_view(), name='user'),

    path('api/auth/login/', ApiLoginView.as_view(), name='api-login'),
    path('api/auth/logout/', ApiLogoutView.as_view(), name='api-logout'),
]