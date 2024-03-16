from django.contrib import admin
from django.urls import path
from QuantifiedSelf import views

urlpatterns = [
    path('', views.home),
]