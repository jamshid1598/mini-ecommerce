from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema

from shop.models import Attribute
from shop.serializers.attribute import AttributeSerializer
from shop.permissions import IsShopMemberOrReadOnly


class AttributeModelViewSet(ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsShopMemberOrReadOnly
    ]
