from django.utils.translation import gettext_lazy as _

# rest-framework
from rest_framework.exceptions import AuthenticationFailed


ADMIN = 'admin'
MANAGER = 'manager'
CLIENT = 'client'

ROLE_CHOICES = (
    (ADMIN, 'Admin'),
    (MANAGER, 'Manager'),
    (CLIENT, 'Client'),
)

ALLOWED_HTTP_METHOD = ['GET', 'HEAD', 'OPTIONS', 'TRACE']
RESTRICTED_HTTP_METHOD = ['POST', 'PUT', 'PATCH', 'DELETE']


def user_access(role=[]):
    def wrapper(func):
        def check(view, request, *args, **kwargs):

            HIERARCHY_ROLES = [
                [ADMIN],
                [ADMIN, MANAGER],
                [ADMIN, MANAGER, CLIENT],
            ]

            if request.method in ALLOWED_HTTP_METHOD and request.user.role in HIERARCHY_ROLES[2]:
                if request.user.role == MANAGER:
                    if not request.user.department:
                        raise AuthenticationFailed({'msg': _("You haven't been assigned to any department")})
                    kwargs['department'] = request.user.department
                return func(view, request, *args, **kwargs)

            if request.method in RESTRICTED_HTTP_METHOD and request.user.role in role:
                if request.user.role == MANAGER:
                    if not request.user.department:
                        raise AuthenticationFailed({'msg': _("You haven't been assigned to any department")})
                    kwargs['department'] = request.user.department
                return func(view, request, *args, **kwargs)

            raise AuthenticationFailed({'msg': _("You haven't been allowed to do this action")})
        return check
    return wrapper
