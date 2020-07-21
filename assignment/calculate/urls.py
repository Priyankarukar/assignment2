from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('calpage',views.calpage,name="calpage"),
    path('check',views.getdata,name="getdata"),
]