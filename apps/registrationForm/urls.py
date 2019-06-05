from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main$', views.loginregister, name='loginregister'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^home$', views.home, name='home'),
    url(r'^logout$', views.logout, name='logout'),
]
