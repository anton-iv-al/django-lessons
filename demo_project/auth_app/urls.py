from django.urls import path
from rest_framework.documentation import include
from rest_framework.routers import DefaultRouter

from .views.logout_view import LogoutView
from .views.unauthorized_view import UnathorizedView
from .views.user_view import UserView
from .views.registration_view import RegistrationView
from .views.login_view import LoginView
from .api.views.users import RegisterView as ApiUsersView
from .api.views.login import LoginView as ApiLoginView
from .api.views.logout import LogoutView as ApiLogoutView
from .api.views.user_current import UserCurrentView as ApiUserCurrentView


user_api_router = DefaultRouter()
user_api_router.register("user", ApiUsersView)

urlpatterns = [
    path('auth/unauthorized/', UnathorizedView.as_view(), name='unauthorized'),
    path('auth/registration/', RegistrationView.as_view(), name='registration'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/user/', UserView.as_view(), name='user'),

    path('api/auth/login/', ApiLoginView.as_view(), name='api-login'),
    path('api/auth/logout/', ApiLogoutView.as_view(), name='api-logout'),

    path('api/auth/user/currenet/', ApiUserCurrentView.as_view(), name='api-user-current'),
    
    path('api/auth/', include(user_api_router.urls), name="api-users"),
]