# django
from django.urls import path

# rest-framework-simplejwt


# local-files
from account.views.token import CustomTokenObtainPairView
from account.views.token_refresh import CustomTokenRefreshView

from account.views.user import (
    UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView, UserCreateAPIView
)


app_name = 'account'


urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('detail/<uuid:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('update/<uuid:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<uuid:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
]


auth_urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
