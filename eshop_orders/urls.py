from django.urls import path
from .views import add_order

app_name = 'eshop_orders'
urlpatterns = [
    path('add-order', add_order, name='add_order'),
]
