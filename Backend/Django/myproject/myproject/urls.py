# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_app/', include('student_app.urls')),
    path('employee/', include('employee_app.urls')),
]