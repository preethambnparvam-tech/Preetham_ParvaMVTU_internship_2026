from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_employee, name='register_employee'),
    path('list/', views.employee_list, name='employee_list'),
]