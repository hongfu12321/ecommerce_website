from django.shortcuts import render

from .models import Customer, Product, Order, OrderItem, ShippingAddress

# Create your views here.

def store(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #Create empty cart for now for none-logged in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}


    context = {
        "items": items,
        "order": order,
    }
    return render(request, 'store/cart.html', context)
    
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #Create empty cart for now for none-logged in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}


    context = {
        "items": items,
        "order": order,
    }
    return render(request, 'store/checkout.html', context)
    