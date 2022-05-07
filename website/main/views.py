from django.shortcuts import render
from .models import Tovar
# Create your views here.

def index(request):
    if 'query' in request.GET:
        q = request.GET['query']
        tovar = Tovar.objects.filter(title__icontains=q)
    else:
        tovar = Tovar.objects.all()
    return render(request, 'main/index.html', {'tovar':tovar})

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



