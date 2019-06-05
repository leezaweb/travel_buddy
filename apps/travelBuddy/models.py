# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..registrationForm.models import User
from django.db import models
from datetime import datetime


class TripManager(models.Manager):

    def validatePost(self, trip):
        errors = []
        date = datetime.now()
        if len(trip["destination"]) < 5:
            errors.append("Please enter destination name")
        if len(trip["description"]) < 10:
            errors.append("Please enter destination description")

        try:
            datetime.strptime(trip["start_date"], "%Y-%m-%d")
            if datetime.strptime(trip["start_date"], "%Y-%m-%d") < date:
                errors.append("Start date has passed")
        except:
            errors.append("Enter a valid start date")


        try:
            datetime.strptime(trip["end_date"], "%Y-%m-%d")
            if datetime.strptime(trip["end_date"], "%Y-%m-%d") < date:
                errors.append("End date has passed")
            if datetime.strptime(trip["end_date"], "%Y-%m-%d") < datetime.strptime(trip["start_date"], "%Y-%m-%d"):
                errors.append("End date is before start date")
        except:
            errors.append("Enter a valid end date")


        return errors

class Trip(models.Model):
    destination=models.CharField(max_length=255)
    planned_by=models.ForeignKey(User, related_name="planner")
    description=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    users=models.ManyToManyField(User, related_name="travellers")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = TripManager()
    def __str__(self):
        return self.destination
