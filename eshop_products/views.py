from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    """
    View for listing all products in the database.
    """
    model = Product
    template_name = 'products/product_list.html'
    paginate_by = 2  # Show "n" products per page

    def get_queryset(self):
        """
         get queryset is a method of ListView class that returns a list of objects to be displayed on the page (in this
            case, active products)
        """
        return Product.objects.get_active_products()
