from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages

from .models import Product
from .forms import ProductForm

def products_list_view(request):
    sale = Product.objects.filter(on_sale=True)
    products = Product.objects.filter(on_sale=False)

    isSaleActive = sale.count() > 0

    sort = 'none'

    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'name':
                sortkey = 'name'
            if sort == 'rating':
                sortkey = '-rating'
            if sort == 'sale':
                sortkey = '-copies_sold'
            products = products.order_by(sortkey)
            
        # if 'q' in request.GET:
        #     query = request.GET['q']
        #     if not query:
        #         messages.error(request, "You didn't enter any search criteria!")
        #         return redirect(reverse('products'))
            
        #     queries = Q(name__icontains=query) | Q(description__icontains=query)
        #     products = products.filter(queries)

    current_sorting = sort

    context = {
        'products': products,
        'sale': sale,
        'isSaleActive': isSaleActive,
        'sortOrder': current_sorting
    }

    return render(request, 'products/products_list.html', context)

def products_detail_view(request, pid):
    product = get_object_or_404(Product, pid=pid)
    isOnSale = product.on_sale == True

    context = {
        'product': product,
        'isOnSale': isOnSale,
    }

    return render(request, 'products/product_detail.html', context)

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

    return redirect(reversed('product_detail', args=[product.pid]))

def products_edit_view(request, pid, *args, **kwargs):
    product = get_object_or_404(Product, pid=pid)
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

def products_delete_view(request, pid, *args, **kwargs):
    product = get_object_or_404(Product, pid=pid)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect(reversed('products_list'))
