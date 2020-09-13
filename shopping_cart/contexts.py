from django.shortcuts import get_object_or_404

from products.models import Product

def shopping_cart(request, *args, **kwargs):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for product_id, product_data in cart.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, id=product_id)
            total += product_data * product.price
            product_count =+ product_data
            cart_items.append({
                'product_id': product_id,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, id=product_id)
            cart_items.append({
                'product_id': product_id,
                'product': product,
            })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
