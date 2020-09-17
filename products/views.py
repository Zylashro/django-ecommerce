from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Product
from .forms import ProductForm

def products_list_view(request):
    allProducts = Product.objects.all()
    sale = allProducts.filter(on_sale=True)
    products = allProducts.filter(on_sale=False)

    isSaleActive = sale.count() > 0

    query = None
    sort = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products_list'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = allProducts.filter(queries)
            isSaleActive = False

        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'name':
                sortkey = 'name'
            if sort == 'rating':
                sortkey = '-rating'
            if sort == 'sale':
                sortkey = '-copies_sold'
            products = products.order_by(sortkey)

    current_sorting = sort

    context = {
        'products': products,
        'sale': sale,
        'isSaleActive': isSaleActive,
        'sortOrder': current_sorting,
        'search': query,
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
