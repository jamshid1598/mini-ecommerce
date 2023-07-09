from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shop.models import Attribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'name', 'image',)


class AttributeFilterSerializer(AttributeSerializer):
    id = serializers.UUIDField(required=False, allow_null=True)
