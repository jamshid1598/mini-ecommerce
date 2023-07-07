import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .manager import UserManager
from .permissions.check_access import ROLE_CHOICES, CLIENT


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(_("username"), max_length=100, unique=True, help_text=_('unique username must be required'))

    role = models.CharField(_("Possition"), max_length=20, choices=ROLE_CHOICES, default=CLIENT)

    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)

    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)

    change_pw = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('username', 'created_at', 'updated_at')
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return "/user/%i/" % (self.pk)
