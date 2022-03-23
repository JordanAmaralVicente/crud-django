from itertools import product
from math import prod
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from .models import Product
from .forms import ProductForm

# Create your views here.
def read_products(request: WSGIRequest):
    products = Product.objects.all()
    return render(
            request,
            'products.html',
            {'products': products},
        )


def create_products(request: WSGIRequest):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('read_products')
    
    return render(request, 'products-form.html', {'form': form})


def update_products(request: WSGIRequest, id: int):
    print(type(request))

    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('read_products')
    
    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_products(request: WSGIRequest, id: int):
    product = Product.objects.get(id=id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('read_products')
    
    return render(request, 'prod-delete-confirm.html', {'product': product})
