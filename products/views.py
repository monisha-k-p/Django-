from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Supplier
from .forms import ProductForm, SupplierForm

def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('home')

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SupplierForm()
    return render(request, 'products/add_supplier.html', {'form': form})
