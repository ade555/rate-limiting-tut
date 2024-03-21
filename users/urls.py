from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import Signup, GetAPIKey

urlpatterns = [
    path('signup/',Signup.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('login/refresh', TokenRefreshView.as_view(), name="login-refresh"),
    path('api_key/get/', GetAPIKey.as_view()),
]
