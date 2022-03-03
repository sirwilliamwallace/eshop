from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    """
    View for listing all products in the database.
    """
    model = Product
    template_name = 'products/product_list.html'
    paginate_by = 10  # Show "n" products per page

    def get_queryset(self):
        """
         get queryset is a method of ListView class that returns a list of objects to be displayed on the page (in this
            case, active products)
        """
        return Product.objects.get_active_products()


def product_detail_view(request, *args, **kwargs):
    """
    View for displaying a single product.
    TODO: make class based view for this view
    """
    product_id = kwargs.get('id')
    product = Product.objects.get_by_id(id=product_id)
    if product is None or not product.active:
        raise Http404("محصول مورد نظر یافت نشد")
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)


class SearchProducts(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 10

    def get_queryset(self):
        """
        get queryset is a method of ListView class that returns a list of objects to be displayed on the page
        """
        query = self.request.GET.get('q')
        search = Product.objects.search(query)  # custom method in models.py to search products by name or description
        return search
