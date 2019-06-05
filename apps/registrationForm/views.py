# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt



def loginregister(request):
    return render(request, "registrationForm/login.html")

def index(request):
    return redirect(reverse("login:loginregister"))

def register(request):
    user = {
    "name": request.POST["name"],
    "username": request.POST["username"],
    "password": request.POST["password"],
    "confirm_password": request.POST["confirm_password"],
    }

    errors = User.objects.validateRegister(user)

    if len(errors) == 0:
        User.objects.create(
        name = user["name"],
        username = user["username"],
        password = bcrypt.hashpw(user["password"].encode(), bcrypt.gensalt())
        )
        request.session["username"]=request.POST["username"]
        return redirect(reverse("travel:travels"))
    else:
        for error in errors:
            messages.warning(request, error)
        return redirect(reverse("login:loginregister"))

def login(request):
    user = {
    "loginusername": request.POST["loginusername"],
    "loginpassword": request.POST["loginpassword"]
    }

    errors = User.objects.validateLogin(user)



    if len(errors) == 0:
        request.session["username"]=request.POST["loginusername"]
        print request.POST["loginusername"]
        print request.session["username"]
        return redirect(reverse("travel:travels"))
    else:
        for error in errors:
            messages.error(request, error)
        return redirect(reverse("login:loginregister"))


def home(request):

    id = User.objects.get(username=request.session["username"]).id


    context={
    "user" : User.objects.get(id=id)
    }
    return redirect(reverse("travel:travels"), context)


def logout(request):
    request.session.clear()
    return redirect(reverse("login:loginregister"))
