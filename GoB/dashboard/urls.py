from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('selection/', views.selection, name='dashboard-selection'),
]
