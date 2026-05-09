"""Fees URLs"""
from django.urls import path
from . import views

app_name = 'fees'

urlpatterns = [
    path('', views.fee_dashboard, name='dashboard'),
    path('list/', views.fee_list, name='fee_list'),
    path('add/', views.fee_create, name='fee_create'),
    path('<uuid:pk>/', views.fee_detail, name='fee_detail'),
    path('<uuid:pk>/pay/', views.fee_pay, name='fee_pay'),
    path('<uuid:pk>/receipt/', views.fee_receipt_pdf, name='receipt_pdf'),
    path('export/csv/', views.export_fees_csv, name='export_csv'),
    path('structure/', views.fee_structure_list, name='structure_list'),
    path('structure/add/', views.fee_structure_create, name='structure_create'),
]
