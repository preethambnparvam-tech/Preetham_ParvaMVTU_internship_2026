from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, index

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
]
