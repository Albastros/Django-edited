# crudapp/urls.py
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add-level/', views.add_level, name="add_level"),  # Add this line for adding new levels
]
