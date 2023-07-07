from django.utils.translation import gettext_lazy as _

# rest_framework
from rest_framework import serializers


def check_password(password, password2):
    if not password == password2:
        raise serializers.ValidationError(_("password didn't match"))
    return True


def validate_passwords(password, password2, **kwargs):
    if kwargs.get('create', None) and kwargs['create']:
        if all([password, password2]):
            return check_password(password, password2)
        raise serializers.ValidationError(_("both password inputs must be filled with the same password"))
    elif kwargs.get('update', None) and kwargs['update']:
        if password or password2:
            return check_password(password, password2)
        return False
