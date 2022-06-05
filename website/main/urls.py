from  django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('delivery', views.delivery, name='delivery'),
    path('basket', views.basket, name='basket'),
    path('authorization', views.authorization, name='authorization'),
    path('registration', views.registration, name='registration'),
    path('order', views.order, name='order'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)