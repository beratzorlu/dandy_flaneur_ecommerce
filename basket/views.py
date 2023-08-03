from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
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
    dimentions = None

    if 'item_dimentions' in request.POST:
        dimentions = request.POST['item_dimentions']
    basket = request.session.get('basket', {})

    if dimentions:
        if item_id in list(basket.keys()):
            if dimentions in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][dimentions] += quantity
                messages.success(request, f'{product.name}: Updated \
                    size {dimentions.upper()} quantity to \
                        {basket[item_id]["items_by_size"][dimentions]}')
            else:
                basket[item_id]['items_by_size'][dimentions] = quantity
                messages.success(request, f'Added size \
                     {dimentions.upper()} {product.name} to your basket')

        else:
            basket[item_id] = {'items_by_size': {dimentions: quantity}}
            messages.success(request, f'Added size \
                 {dimentions.upper()} {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated \
                 {product.name} quantity to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def edit_basket(request, item_id):
    """
    Edit quantity of selected items and remove items from the basket
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    dimentions = None
    if 'item_dimentions' in request.POST:
        dimentions = request.POST['item_dimentions']
    basket = request.session.get('basket', {})

    if not product:
        messages.error(request, 'Product does not exist')
        return redirect(reverse('view_basket'))

    if dimentions:
        if quantity > 0:
            basket[item_id]['items_by_size'][dimentions] = quantity
            messages.success(
                request, f'Updated size {dimentions.upper()} {product.name}\
                     quantity to \
                        {basket[item_id]["items_by_size"][dimentions]}')
        else:
            del basket[item_id]['items_by_size'][dimentions]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(
                    request, f'Removed size {dimentions.upper()} \
                        {product.name} from your basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to\
                     {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_basket(request, item_id):
    """Remove the items from basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        dimentions = None
        if 'item_dimentions' in request.POST:
            size = request.POST['item_dimentions']
        basket = request.session.get('basket', {})

        if dimentions:
            del basket[item_id]['items_by_size'][dimentions]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(request, f'Removed size \
                     {dimentions.upper()} {product.name} from your basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your \
                 basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
