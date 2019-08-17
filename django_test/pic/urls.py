from django.conf.urls import url
from django.contrib import admin
from pic import views

urlpatterns = [
    url(r'', views.up_file)
]