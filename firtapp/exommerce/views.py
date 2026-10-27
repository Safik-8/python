from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Cart, CartItem


# ─────────────────────────────────────────────
# HOME
# ─────────────────────────────────────────────
def home(request):
    featured = Product.objects.filter(stock__gt=0).order_by('-created_at')[:6]
    context = {'featured_products': featured}
    return render(request, 'exommerce/home.html', context)


# ─────────────────────────────────────────────
# PRODUCTS – LIST (and detail by id)
# ─────────────────────────────────────────────
def products(request):
    all_products = Product.objects.all().order_by('-created_at')
    return render(request, 'exommerce/products.html', {'products': all_products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'exommerce/product_detail.html', {'product': product})


# ─────────────────────────────────────────────
# PRODUCT CRUD
# ─────────────────────────────────────────────
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        price = request.POST.get('price', '0')
        stock = request.POST.get('stock', '0')
        image_url = request.POST.get('image_url', '').strip()

        if name and price:
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                stock=stock,
                image_url=image_url,
            )
            messages.success(request, f'"{name}" has been added successfully!')
            return redirect('products')
        else:
            messages.error(request, 'Name and Price are required.')

    return render(request, 'exommerce/product_form.html', {'action': 'Add'})


def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name', product.name).strip()
        product.description = request.POST.get('description', product.description).strip()
        product.price = request.POST.get('price', product.price)
        product.stock = request.POST.get('stock', product.stock)
        product.image_url = request.POST.get('image_url', product.image_url).strip()
        product.save()
        messages.success(request, f'"{product.name}" updated successfully!')
        return redirect('products')

    return render(request, 'exommerce/product_form.html', {'action': 'Edit', 'product': product})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        name = product.name
        product.delete()
        messages.success(request, f'"{name}" deleted successfully.')
        return redirect('products')
    return render(request, 'exommerce/product_confirm_delete.html', {'product': product})


# ─────────────────────────────────────────────
# CART HELPERS
# ─────────────────────────────────────────────
def _get_or_create_cart(request):
    if not request.session.session_key:
        request.session.create()
    cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart


# ─────────────────────────────────────────────
# CART VIEWS
# ─────────────────────────────────────────────
def cart_view(request):
    cart = _get_or_create_cart(request)
    items = cart.items.select_related('product').all()
    return render(request, 'exommerce/cart.html', {'cart': cart, 'items': items})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = _get_or_create_cart(request)

    if product.stock < 1:
        messages.error(request, f'Sorry, "{product.name}" is out of stock.')
        return redirect('products')

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'"{product.name}" quantity updated in cart.')
        else:
            messages.warning(request, f'Cannot add more – only {product.stock} in stock.')
    else:
        messages.success(request, f'"{product.name}" added to cart!')

    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'"{name}" removed from cart.')
    return redirect('cart')


def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    qty = int(request.POST.get('quantity', 1))
    if qty < 1:
        cart_item.delete()
        messages.success(request, 'Item removed from cart.')
    else:
        cart_item.quantity = min(qty, cart_item.product.stock)
        cart_item.save()
        messages.success(request, 'Cart updated.')
    return redirect('cart')


# ─────────────────────────────────────────────
# ABOUT
# ─────────────────────────────────────────────
def about(request):
    return render(request, 'exommerce/about.html')
