from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shop.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'image',)

    def to_representation(self, instance):
        data = super(CategorySerializer, self).to_representation(instance)
        data['children'] = instance.categories.values('id', 'name')
        return data

    def validate(self, attrs):
        parent = attrs.get('parent')
        if parent and parent.has_product:
            error_msg = f"This {parent.name} category can't be " \
            "used as parent category becouse it has products."
            raise ValidationError(_(error_msg))

        return attrs
