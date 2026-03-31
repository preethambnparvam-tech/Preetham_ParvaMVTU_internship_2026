from django.urls import path
from . import views

urlpatterns = [
    # Call the method when we hit the route
    path('', views.welcome, name='welcome'),
    path('greet/', views.greet, name='greet'),
    path('bye/', views.bye, name='bye'),
]