# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login as Login, logout as Logout
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser


def login(request):

    if  not isinstance(request.user, AnonymousUser):
        return render(request, 'home.html')

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                Login(request, user)
                return render(request, 'home.html')

        messages.add_message(request, messages.ERROR, u"Usuário e/ou senha incorreto(s).")

    return render(request, 'login.html')


def logout(request):
    Logout(request)
    return render(request, 'login.html')
