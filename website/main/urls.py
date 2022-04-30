
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('delivery', views.delivery, name='delivery'),
    path('basket', views.basket, name='basket'),
    path('authorization', views.authorization, name='authorization')
]