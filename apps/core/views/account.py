from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from account.models import User


def user_list(request, *args, **kwargs):
    users = User.objects.all()
    return render(request, 'account/user_list.html', {'users': users})
