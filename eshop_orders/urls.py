from django.urls import path
from .views import add_order, card_detail

app_name = 'eshop_orders'
urlpatterns = [
    path('add-order', add_order, name='add_order'),
    path('order-detail', card_detail, name='order_detail'),
]
