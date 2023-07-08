# rest-framework-simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# local-files
from account.serializers.token_refresh import CustomTokenRefreshSerializer
from account.serializers.token import CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
