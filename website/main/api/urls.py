from django.urls import re_path

from . import views
app_name = 'main'
urlpatterns = [
    re_path(r'^orders/$', views.OrderListView.as_view(), name='order_list'),
    re_path(r'^orders/(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='order_detail'),
]