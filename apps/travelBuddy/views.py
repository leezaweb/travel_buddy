# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..registrationForm.models import User
from .models import Trip

def travels(request):
    id = User.objects.get(username=request.session["username"]).id
    context={
    "user" : User.objects.get(id=id),
    "planner" :Trip.objects.filter(planned_by=id)|Trip.objects.filter(users=User.objects.get(id=id)).order_by("start_date"),
    "travellers" :Trip.objects.exclude(planned_by=id).order_by("start_date")
    }
    return render(request, "travelBuddy/index.html", context)

def destination(request,tripid):
    context={
    "trips" :Trip.objects.filter(id=tripid),
    "travellers": User.objects.filter(travellers__id__in=Trip.objects.filter(id=tripid))
    }
    return render(request, "travelBuddy/destination.html", context)


def add(request):
    return render(request, "travelBuddy/add.html")

def join(request,tripid):
    Trip.objects.get(id=tripid).users.add(User.objects.get(username=request.session["username"]))
    Trip.objects.get(id=tripid).save()
    messages.info(request, "Congratulations! You joined a trip")
    return redirect(reverse("travel:travels"))


def post(request):
    id = User.objects.get(username=request.session["username"]).id

    trip = {
    "destination": request.POST["destination"],
    "planned_by": User.objects.get(id=id),
    "description": request.POST["description"],
    "start_date": request.POST["start_date"],
    "end_date": request.POST["end_date"]
    }

    errors = Trip.objects.validatePost(trip)

    if len(errors) == 0:
        Trip.objects.create(
        destination = trip["destination"],
        planned_by = trip["planned_by"],
        description = trip["description"],
        start_date = trip["start_date"],
        end_date = trip["end_date"]
        )
        messages.info(request, "Congratulations! You added a trip")
        return redirect(reverse("travel:travels"))
    else:
        for error in errors:
            messages.info(request, error)
        return redirect(reverse("travel:add"))
