from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models import (
    Category, Product, Attribute
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    list_filter = ('name', 'parent',)
    list_display_links = ('name', 'parent',)


class AttributeInline(admin.TabularInline):
    model = Attribute


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [AttributeInline]
    list_display = ('name', 'category',)
    list_filter = ('name', 'category',)
    list_display_links = ('name', 'category',)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'price')
    list_filter = ('name', 'product', 'price')
    list_display_links = ('name', 'product', 'price')
