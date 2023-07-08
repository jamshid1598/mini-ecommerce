import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from account.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(_("username"), max_length=100, unique=True, help_text=_('unique username must be required'))

    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)

    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = "account_users"
        ordering = ('username', 'created_at', 'updated_at')
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return "/user/%i/" % (self.pk)


class BaseModel(models.Model):
    cleated_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey('account.User', blank=True, null=True, 
                                   on_delete=models.SET_NULL, related_name='created_%(model_name)ss')
    updated_by = models.ForeignKey('account.User', blank=True, null=True, 
                                   on_delete=models.SET_NULL, related_name='updated_%(model_name)ss')

    @property
    def class_name(self):
        return self.__class__.__name__

    class Meta:
        abstract = True
        ordering = ['id']


class ShopMember(BaseModel):
    class MembersRole(models.TextChoices):
        ADMIN = "admin", _("Admin")
        MANAGER = "manager", _("Manager")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE,
                             related_name='shop_members', verbose_name=_("Shop Member"))
    role = models.CharField(_("Role"), max_length=255, choices=MembersRole.choices, default=MembersRole.MANAGER)

    class Meta:
        db_table = "account_shop_members"
        ordering = ["user"]
        verbose_name = _("Shop Member")
        verbose_name_plural = _("Shop Members")

    def __str__(self):
        try:
            return self.user.username
        except:
            return self.user.id
