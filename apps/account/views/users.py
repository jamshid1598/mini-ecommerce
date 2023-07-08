from django.utils.translation import gettext_lazy as _
from rest_framework import (
    generics, permissions, status
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from drf_spectacular.utils import extend_schema

# local-files
from account.models import User, ShopMember
from account.serializers.users import (
    UserSerializer, UserCreateUpdateSerializer,
    ShopMemberSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=['api.users'])
    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(request, *args, **kwargs)

    @extend_schema(tags=['api.users'])
    def retrieve(self, request, *args, **kwargs):
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    @extend_schema(tags=['api.users'])
    def destroy(self, request, *args, **kwargs):
        return super(UserViewSet, self).destroy(request, *args, **kwargs)


class UserCreateAPIView(APIView):

    @extend_schema(
        request=UserCreateUpdateSerializer,
        responses={201: UserSerializer},
        tags=['api.users'],
    )
    def post(self, request, *args, **kwargs):
        serializer = UserCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserUpdateAPIView(APIView):

    @extend_schema(
        request=UserCreateUpdateSerializer,
        responses={200: UserSerializer},
        tags=['api.users'],
    )
    def put(self, request, pk, *args, **kwargs):
        instance = generics.get_object_or_404(User, pk=pk)
        serializer = UserCreateUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShopMemberViewSet(ModelViewSet):
    queryset = ShopMember.objects.all()
    serializer_class = ShopMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=['api.shop_member'])
    def list(self, request, *args, **kwargs):
        return super(ShopMemberViewSet, self).list(request, *args, **kwargs)

    @extend_schema(tags=['api.shop_member'])
    def create(self, request, *args, **kwargs):
        user = ShopMember.objects.filter(user=request.user)
        admin = user.exists() and user.first().role == 'admin'
        if not (admin or request.user.is_superuser):
            raise PermissionDenied(_('Only admin users can create Shop-Members'))
        return super(ShopMemberViewSet, self).create(request, *args, **kwargs)

    @extend_schema(tags=['api.shop_member'])
    def retrieve(self, request, *args, **kwargs):
        return super(ShopMemberViewSet, self).retrieve(request, *args, **kwargs)

    @extend_schema(tags=['api.shop_member'])
    def update(self, request, *args, **kwargs):
        return super(ShopMemberViewSet, self).update(request, *args, **kwargs)

    @extend_schema(tags=['api.shop_member'])
    def partial_update(self, request, *args, **kwargs):
        return super(ShopMemberViewSet, self).partial_update(request, *args, **kwargs)

    @extend_schema(tags=['api.shop_member'])
    def destroy(self, request, *args, **kwargs):
        return super(ShopMemberViewSet, self).destroy(request, *args, **kwargs)
