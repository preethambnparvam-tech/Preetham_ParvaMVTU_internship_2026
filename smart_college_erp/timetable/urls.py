"""Timetable URLs"""
from django.urls import path
from . import views

app_name = 'timetable'

urlpatterns = [
    path('', views.timetable_view, name='view'),
    path('add/', views.timetable_create, name='create'),
    path('<uuid:pk>/delete/', views.timetable_delete, name='delete'),
    path('timeslot/add/', views.timeslot_create, name='timeslot_create'),
]
