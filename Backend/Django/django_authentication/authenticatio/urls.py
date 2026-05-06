from django.urls import path
from .import views

urlpatterns = [
    path('register', views.user_register, name='signup'),
    path('login', views.user_login, name='signin'),
    path('logout', views.user_logout, name='signout'),
    path('dashboard', views.user_dashboard, name='welcome'),
]