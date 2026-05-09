from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # Departments
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_create, name='department_create'),
    path('departments/<uuid:pk>/edit/', views.department_edit, name='department_edit'),
    path('departments/<uuid:pk>/delete/', views.department_delete, name='department_delete'),

    # Students
    path('', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('<uuid:pk>/', views.student_detail, name='student_detail'),
    path('<uuid:pk>/edit/', views.student_edit, name='student_edit'),
    path('<uuid:pk>/delete/', views.student_delete, name='student_delete'),

    # Exports
    path('export/csv/', views.export_students_csv, name='export_csv'),
    path('export/pdf/', views.export_students_pdf, name='export_pdf'),

    # Courses
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_create'),
    path('courses/<uuid:pk>/edit/', views.course_edit, name='course_edit'),
]
