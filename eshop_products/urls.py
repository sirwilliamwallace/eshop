from django.urls import path

from .views import ProductListView, product_detail_view

app_name = 'eshop_products'
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<id>/<title>', product_detail_view, name='product_detail'),
]
