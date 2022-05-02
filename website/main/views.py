from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def delivery(request):
    return render(request, 'main/delivery.html')

def basket(request):
    return render(request, 'main/basket.html')

def authorization(request):
    return render(request, 'main/authorization.html')

def registration(request):
    return render(request, 'main/registration.html')
