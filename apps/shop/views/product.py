from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema

from shop.models import Product
from shop.serializers.product import ProductSerializer
from shop.permissions import IsShopMemberOrReadOnly


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsShopMemberOrReadOnly
    ]

    @extend_schema(description="`id` field of the newly created attribute musn't be removed from request body.")
    def create(self, request, *args, **kwargs):
        return super(ProductModelViewSet, self).create(request, *args, **kwargs)

    @extend_schema(description="`id` field of the newly created attribute musn't be removed from request body.")
    def update(self, request, *args, **kwargs):
        return super(ProductModelViewSet, self).update(request, *args, **kwargs)

    @extend_schema(description="`id` field of the newly created attribute musn't be removed from request body.")
    def partial_update(self, request, *args, **kwargs):
        return super(ProductModelViewSet, self).partial_update(request, *args, **kwargs)
