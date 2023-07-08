# django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# local-files
from account.views.auth import (
    CustomTokenObtainPairView, CustomTokenRefreshView,
)
from account.views.users import (
    UserUpdateAPIView, UserCreateAPIView,
    UserViewSet, ShopMemberViewSet,
)


app_name = 'account'


user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})


router = DefaultRouter()
router.register(r'shop-member', ShopMemberViewSet, basename='shop-member')


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    path('list/', user_list, name='user-list'),
    path('detail/<uuid:pk>/', user_detail, name='user-detail'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('update/<uuid:pk>/', UserUpdateAPIView.as_view(), name='user-update'),

    path('', include(router.urls)),
]
