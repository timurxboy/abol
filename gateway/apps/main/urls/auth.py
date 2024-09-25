from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from apps.main.views import RegisterView, DeleteView, ChangePasswordView, UpdateProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('update/', UpdateProfileView.as_view(), name='update_profile'),
    path('delete/', DeleteView.as_view(), name='delete'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
]
