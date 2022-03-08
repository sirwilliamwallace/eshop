import itertools

from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product , Gallery
from eshop_products_categories.models import ProductsCategories
from eshop_orders.forms import OrderForm

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


class ProductCategoriesListView(ListView):
    """
    View for listing all products in the database.
    This view is used to display products in a category.
    """
    template_name = 'products/product_list.html'  # Default template name
    paginate_by = 10  # Show "n" products per page

    def get_queryset(self):  # Override the get_queryset method
        """
         get queryset is a method of ListView class that returns a list of objects to be displayed on the page (in this
            case, active products)
        """
        category_name = self.kwargs['category']  # Get the category name from the URL
        category = ProductsCategories.objects.filter(slug__iexact=category_name).filter()  # Get the category object
        # print(category)
        if category is None:  # If the category does not exist
            raise Http404("صفحه مورد نظر یافت نشد")  # Raise an error
        return Product.objects.get_product_by_categories(
            categorie_name=category_name)  # Return the products in the category


def gallery_iterate(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail_view(request, *args, **kwargs):
    """
    View for displaying a single product.
    TODO: make class based view for this view
    """
    product_id = kwargs.get('id')
    order_form = OrderForm(request.POST or None, initial={'productId': product_id})
    product = Product.objects.get_by_id(id=product_id)
    if product is None or not product.active:
        raise Http404("محصول مورد نظر یافت نشد")

    gallery = Gallery.objects.filter(product_id=product_id)
    iterated_galleries = list(gallery_iterate(3, gallery))
    
    recommended_products = Product.objects.get_queryset().filter(categories__product=product).distinct()
    iterated_recommended_products = list(gallery_iterate(3,recommended_products))
    
    context = {
        'product': product,
        'galleries': iterated_galleries,
        'related_products': iterated_recommended_products,
        'new_order_form': order_form,
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


def category_partial_view(request, *args, **kwargs):
    """
    View for sending data to the template for displaying the categories in the sidebar.
    """
    categories = ProductsCategories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/category_partial.html', context)
