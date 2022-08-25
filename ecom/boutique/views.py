from math import prod
from django.shortcuts import get_object_or_404, render

#from cart.forms import CartAddProductForm
#from ecom.boutique.models import Product

from .models import Category, Product
# Create your views here.


def store(request):
    context = {}
    return render(request, 'boutique/store.html', context)

def cart(request):
    context = {}
    return render(request, 'boutique/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'boutique/checkout.html', context)

def main(request):
    context = {}
    return render(request, 'boutique/main.html', context)



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'boutique/product/list.html',{'category': category,
                                                    'categories': categories,
                                                    'products': products})
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    #cart_product_from = CartAddProductForm()
    return render(request, 'ecom/boutique/detail.html', {'product': product, 'cart_product_from': cart_product_from})