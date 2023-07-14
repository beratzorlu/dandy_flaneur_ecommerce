from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from store.models import Product, Category


def view_basket(request):
    """Renders the basket contents page"""

    products = Product.objects.all()
    all_categories = Category.objects.all()

    context = {
        'products': products,
        'all_categories': all_categories
    }

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """Add a chosen quantity of selected products to the shopping basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'item_dimentions' in request.POST:
        size = request.POST['item_dimentions']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} to {basket[item_id]["items_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your basket')

        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)
