# django
from django.contrib.auth import get_user_model

# local-files
from account.utils.validate_password import validate_passwords

User = get_user_model()


def update_create_user(user_validated_data, user=None, **kwargs):
    password = user_validated_data.pop('password', None)
    password2 = user_validated_data.pop('password2', None)

    if kwargs.get('update', None) and kwargs['update'] and user:
        user.username = user_validated_data.get('username', user.username)
        user.role = user_validated_data.get('role', user.role)

        if validate_passwords(password, password2, **{'update': True}):
            user.set_password(password)
        user.save()

    else:
        if validate_passwords(password, password2, **{'create': True}):
            user = User(**user_validated_data)
            user.set_password(password)
            user.save()
    return user
