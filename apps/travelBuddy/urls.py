from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^travels$", views.travels, name="travels"),
    url(r"^destination/(?P<tripid>\d+)$", views.destination, name="destination"),
    url(r"^add$", views.add, name="add"),
    url(r"^join/(?P<tripid>\d+)$", views.join),
    url(r"^post$", views.post, name="post"),
]
