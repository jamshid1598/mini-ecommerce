# django
from django.utils.translation import gettext_lazy as _

# rest-framework
from rest_framework import serializers

# local-files
from account.models import User
from account.utils.validate_password import validate_passwords


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'role']


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, style={'input_type': 'password'}, trim_whitespace=False)
    password2 = serializers.CharField(required=False, style={'input_type': 'password'}, trim_whitespace=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'role', 'password', 'password2',)
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def to_representation(self, value):
        data = super().to_representation(value)
        if data.get('password', None):
            del data['password']
        if data.get('password2', None):
            del data['password2']
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2', None)

        if validate_passwords(password, password2, **{'create': True}):
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user
        return None

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2', None)

        instance.username = validated_data.get('username', instance.username)
        instance.role = validated_data.get('role', instance.role)

        if validate_passwords(password, password2, **{'update': True}):
            instance.set_password(password)

        instance.save()
        return instance
