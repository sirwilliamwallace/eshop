from django.urls import path

from .views import ProductListView, product_detail_view, SearchProducts

app_name = 'eshop_products'
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<id>/<title>', product_detail_view, name='product_detail'),
    path('products/search',SearchProducts.as_view() , name='search_products'),
]
