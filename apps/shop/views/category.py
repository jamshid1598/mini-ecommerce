from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema

from shop.models import Category
from shop.serializers.category import CategorySerializer
from shop.permissions import IsShopMemberOrReadOnly


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsShopMemberOrReadOnly
    ]
