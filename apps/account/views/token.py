# rest-framework-simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView

# local-files
from account.serializers.token import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
