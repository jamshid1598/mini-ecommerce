# django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# local-files
from shop.views.category import CategoryModelViewSet
from shop.views.product import ProductModelViewSet
from shop.views.attribute import AttributeModelViewSet


app_name = 'shop'


router = DefaultRouter()
router.register(r'category', CategoryModelViewSet, basename='category')
router.register(r'product', ProductModelViewSet, basename='product')
router.register(r'attribute', AttributeModelViewSet, basename='attribute')

# category_list = CategoryModelViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# category_detail = CategoryModelViewSet.as_view({
#     'get': 'retrieve',
#     'delete': 'destroy',
#     'put': 'update',
#     'putch': 'partial_update',
# })

urlpatterns = [
    path('', include(router.urls)),
]
