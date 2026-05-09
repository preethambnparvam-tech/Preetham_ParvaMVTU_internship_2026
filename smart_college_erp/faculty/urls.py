"""Faculty URLs"""
from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
    path('', views.faculty_list, name='faculty_list'),
    path('add/', views.faculty_create, name='faculty_create'),
    path('<uuid:pk>/', views.faculty_detail, name='faculty_detail'),
    path('<uuid:pk>/edit/', views.faculty_edit, name='faculty_edit'),
    path('<uuid:pk>/delete/', views.faculty_delete, name='faculty_delete'),
    path('export/csv/', views.export_faculty_csv, name='export_csv'),
]
