from django.urls import path

from .views import ProductListView

app_name = 'eshop_products'
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
]