"""
Smart College ERP - Root URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # App URLs
    path('students/', include('students.urls', namespace='students')),
    path('faculty/', include('faculty.urls', namespace='faculty')),
    path('attendance/', include('attendance.urls', namespace='attendance')),
    path('fees/', include('fees.urls', namespace='fees')),
    path('timetable/', include('timetable.urls', namespace='timetable')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
