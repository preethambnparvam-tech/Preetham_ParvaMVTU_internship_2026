from rest_framework import viewsets
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer

def index(request):
    return render(request, 'product-management_app/index.html')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
