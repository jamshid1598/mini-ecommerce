from django.urls import path
from core.views.account import user_list


app_name = 'core_accout'

urlpatterns = [
    path('list/', user_list, name='user-list'),
]
