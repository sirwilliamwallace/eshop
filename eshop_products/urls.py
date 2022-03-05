from django.urls import path

from .views import ProductListView, product_detail_view, SearchProducts, ProductCategoriesListView, category_partial_view

app_name = 'eshop_products'
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<id>/<title>', product_detail_view, name='product_detail'),
    path('products/search', SearchProducts.as_view(), name='search_products'),
    path('products/<category>/', ProductCategoriesListView.as_view(), name='category_products'),
    path('categories_partial_view', category_partial_view, name='category_partial_view'),
]
