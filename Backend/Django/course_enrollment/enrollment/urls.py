
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='list_students'),
    path('add_student/', views.create_student, name='add_student'),
    path('edit_student/<int:id>', views.update_student, name='edit_student'),
    path('delete_student/<int:id>', views.remove_student, name='delete_student'),
    path('list_courses/', views.course_list, name='list_courses'),
    path('add_course/', views.create_course, name='add_course'),
    path('edit_course/<int:id>', views.update_course, name='edit_course'),
    path('delete_course/<int:id>', views.remove_course, name='delete_course'),
    path('deleted_course/', views.deleted_courses, name='deleted_course'),
    path('course_restore/<int:id>', views.restore_course, name='course_restore'),
    path('list_enrollments/', views.enrollment_list, name='list_enrollments'),
    path('enroll/', views.enroll_course, name='course_enrollment'),
]