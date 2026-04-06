from django.urls import path
from .import views

# 127.0.0.1:8000/student_app

urlpatterns = [
    # Route for listing the data from db  -- # Link: 127.0.0.1:8000/student_app/
    path('', views.student_list, name="list_of_students"),
    # Route for creating or inserting the data in db  -- # Link: 127.0.0.1:8000/student_app/form/
    path('form/', views.student_form, name="registration_form"),
    # Route for viewing the individual data from db by referring the primary key -- # Link: 127.0.0.1:8000/student_app/1/
    path('<int:pk>/', views.student_info, name="student_details"),
    # Route for updating the existing data in db by referring the primary key  -- # Link: 127.0.0.1:8000/student_app/1/edit/
    path('<int:pk>/edit', views.edit_student, name="update_details"),
    # Route for deleting the existing data in db by referring the primary key  -- # Link: 127.0.0.1:8000/student_app/1/delete/
    path('<int:pk>/delete', views.delete_student, name="remove_student"),
]

# Named Routes: list_of_students, registration_form, student_details, update_details, remove_student, we will use this in anchor tag links