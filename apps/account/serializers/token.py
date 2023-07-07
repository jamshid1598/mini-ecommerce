from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..permissions.check_access import MANAGER


def get_department(user):
    if user.role == MANAGER and user.department:
        return user.department.id
    return None


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        data["username"] = self.user.username
        data["role"] = self.user.role
        data['department'] = get_department(self.user)

        return data
