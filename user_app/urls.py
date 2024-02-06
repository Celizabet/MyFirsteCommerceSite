from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import registration_view, logout_view, user_profile_registration_view

urlpatterns = [
    #path("login/", obtain_auth_token), #Vista por default
    path("register/", registration_view),
    #path("logout/", logout_view)

    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
    path("profile-token", user_profile_registration_view)
]