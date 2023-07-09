from rest_framework import permissions

from account.models import ShopMember


class IsShopMemberOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the users with admin and manager role or superuser.
        roles = [x[0] for x in ShopMember.MembersRole.choices]
        shop_member = ShopMember.objects.filter(user=request.user).first()
        shopmember = shop_member and shop_member.role in roles
        if shopmember or request.user.is_superuser:
            return True
