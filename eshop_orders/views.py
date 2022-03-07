from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
from eshop_orders.forms import OrderForm
from eshop_orders.models import Order
from eshop_products.models import Product


@login_required(login_url='eshop_account:login')
def add_order(request):
    order_form = OrderForm(request.POST or None)
    if order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, isPaid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, isPaid=False)
        productId = order_form.cleaned_data['productId']
        tedad = order_form.cleaned_data['tedad']
        if tedad <= 0:
            tedad = 1
        product = Product.objects.get_by_id(productId)
        order.orderdetail_set.create(product_id=product.id, gheymat=product.price * tedad, tedad=tedad)
        # felan redirecte maskhare
        title_product = product.title.replace(' ', '-')
        return redirect(f'/products/{productId}/{title_product}')
    return redirect(f'eshop_products:product_list')
