# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):

    def validateRegister(self, user):
        errors = []
        if len(user["name"]) < 3 or not user["name"]:
            errors.append("Name: Required; Use no fewer than 2 characters; letters only")
        if len(user["username"]) < 3:
            errors.append("Username: Required; Use no fewer than 2 characters")
        if len(user["password"]) < 8:
            errors.append("Password: Required; No fewer than 8 characters in length")
        if user["password"] !=user["confirm_password"]:
            errors.append("Passwords must match")

        return errors
    def validateLogin(self, user):
        errors = []
        try:
            userid = User.objects.get(username=user["loginusername"]).id
            if bcrypt.checkpw(user["loginpassword"].encode(), User.objects.get(id=userid).password.encode())!=True:
                errors.append("Wrong Password")
        except:
            errors.append("No such user")


        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.name
