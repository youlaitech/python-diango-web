# coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add),
    url(r'^edit/$', views.edit),
    url(r'^delete/$', views.delete)
]
