from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages

from .models import Product
from .forms import ProductForm

def products_list_view(request, *args, **kwargs):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, context)

def products_detail_view(request, _id, *args, **kwargs):
    product = get_object_or_404(Product, id=_id)

    context = {
        'product': product,
    }

    return render(request, context)

def banner_products_view(request, on_sale, *args, **kwargs):
    products = Product.objects.filter(on_sale=True)[:3]

    context = {
        'products': products,
    }

    return render(request, context)

def products_create_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product created!')
            return redirect(reversed('product_detail', args=[product._id]))
        else:
            messages.error(request, 'Failed to create product.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, context)

def products_edit_view(request, _id, *args, **kwargs):
    product = get_object_or_404(Product, id=_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated!')
        else:
            messages.error(request, 'Failed to update product.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, context)

def products_delete_view(request, _id, *args, **kwargs):
    product = get_object_or_404(Product, id=_id)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect(reversed('products_list'))
