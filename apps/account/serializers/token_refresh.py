# rest-framework-simplejwt
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from ..permissions.check_access import MANAGER


class CustomTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        return data
