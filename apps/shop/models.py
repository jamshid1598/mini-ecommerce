import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# local files
from account.models import BaseModel


class Category(BaseModel):
    id = models.UUIDField(_('ID'), primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                               related_name='categories', verbose_name=_('Parent Category'))
    name = models.CharField(_('Name'), max_length=255)
    image = models.ImageField(_('Image'), upload_to='category/images/', blank=True, null=True)

    @property
    def child_ids(self):
        pass

    @property
    def child_categories(self):
        return self.categories.all().values('id', 'name')

    @property
    def parent_hierarchy(self):
        return []

    @property
    def has_product(self):
        return self.products.all().count() > 0

    @property
    def has_shild_categories(self):
        return self.categories.all().count() > 0

    def __str__(self):
        return self.name

    class Meta:
        db_table = "shop_category"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(BaseModel):
    id = models.UUIDField(_('ID'), primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    category = models.ForeignKey('shop.Category', on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='products', verbose_name=_('Category'),)
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Image'), upload_to='product/images/', blank=True, null=True)

    class Meta:
        db_table = "shop_product"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Attribute(BaseModel):
    id = models.UUIDField(_('Id'), primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='attributes',
                                verbose_name=_('Product'))
    price = models.FloatField(_('Price'), default=0.0)
    name = models.CharField(_('Name'), max_length=255)
    image = models.ImageField(_('Image'), upload_to='attributes/images/', blank=True, null=True)

    class Meta:
        db_table = "shop_attribute"
        verbose_name = _("Attribute")
        verbose_name_plural = _("Attributes")

    def __str__(self):
        return self.name
