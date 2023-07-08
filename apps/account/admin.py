from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, ShopMember


class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (_('User Info'),
            {'fields': (
                "username",
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

    list_display = ('username', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'updated_at', 'created_at',)
    list_display_links = ('username',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'updated_at', 'created_at',)
    search_fields = ('username',)
    ordering = ('username', 'is_staff', 'is_superuser', 'is_active', 'updated_at', 'created_at', )
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)


@admin.register(ShopMember)
class ShopMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'role',)
