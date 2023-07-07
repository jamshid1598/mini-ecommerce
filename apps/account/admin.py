from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (_('User Info'),
            {'fields': (
                "username",
                'role',
                'department',
            )
        }),
        (_('Status/Groups/Permissions'),
            {'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )

    add_fieldsets = (
        (_("create new user"), {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
    )

    list_display = ('username', 'role', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'updated_at', 'created_at',)
    list_display_links = ('username',)
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'updated_at', 'created_at',)
    search_fields = ('username',)
    ordering = ('username', 'role', 'is_staff', 'is_superuser', 'is_active', 'updated_at', 'created_at', )
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
