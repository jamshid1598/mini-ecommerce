# other packages
from rest_framework_simplejwt.views import TokenRefreshView

# local-files
from ..serializers.token_refresh import CustomTokenRefreshSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
