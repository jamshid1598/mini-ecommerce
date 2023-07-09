from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shop.models import Product, Attribute
from shop.serializers.attribute import AttributeFilterSerializer


class ProductSerializer(serializers.ModelSerializer):
    attributes = serializers.ListField(
        child=AttributeFilterSerializer(), max_length=100,
        allow_empty=False, write_only=True)
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'description', 'image', 'attributes',)

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        data['attributes'] = instance.attributes.values('id', 'name', 'image')
        return data

    def validate(self, attrs):
        category = attrs.get('category')
        if category and category.has_shild_categories:
            error_msg = f"This {category.name} category can't be " \
            "used as product category becouse it has child chategory."
            raise ValidationError(_(error_msg))

        return attrs
    
    def create(self, validated_data):
        attributes = validated_data.pop('attributes', [])
        product = Product.objects.create(**validated_data)

        for attribute in attributes:
            Attribute.objects.create(
                **attribute,
                product=product
            )
        return product

    def update(self, instance, validated_data):
        attributes = validated_data.pop('attributes', [])

        current_attributes_ids = list(Attribute.objects.filter(product=instance).values_list('id', flat=True))
        for attribute in attributes:
            id = attribute.get('id')
            if id and id in current_attributes_ids:
                current_attributes_ids.remove(id)
                Attribute.objects.filter(product=instance, id=id).update(**attribute)
            else:
                Attribute.objects.create(**attribute, product=instance)
        Attribute.objects.filter(id__in=current_attributes_ids).delete()

        return super(ProductSerializer, self).update(instance, validated_data)

        # instance.name = validated_data.get("name", instance.name)
        # instance.save()
