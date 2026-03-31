from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "demo/index.html")

def greet(request):
    return render(request, "demo/greet.html")

def bye(request):
    return render(request, "demo/bye.html")