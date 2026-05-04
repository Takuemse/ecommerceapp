from django.shortcuts import render, redirect
# ↑ render = show a page
# ↑ redirect = send user to another page

from django.contrib import messages
# ↑ used to show success/error messages

from .models import Product
# ↑ import our Product so we can use it

from .forms import OrderForm
# ↑ import our Order Form (we'll create this next step)


# ═══════════════════════════════
# VIEW 1 — Homepage
# ═══════════════════════════════
def homepage(request):
    # request = the visitor knocking on the door
    
    return render(request, 'store/homepage.html')
    # ↑ open the door and show them homepage.html


# ═══════════════════════════════
# VIEW 2 — Products Page
# ═══════════════════════════════
def product_list(request):
    
    products = Product.objects.all()
    # ↑ go to the database and get ALL products
    # like asking the kitchen for the full menu
    
    return render(request, 'store/product_list.html', {'products': products})
    # ↑ show product_list.html AND send the products to it
    # {'products': products} is like putting the menu in a bag
    # and handing it to the waiter (template)


# ═══════════════════════════════
# VIEW 3 — Cart Page
# ═══════════════════════════════
def cart(request):
    
    cart = request.session.get('cart', {})
    # ↑ session = Django's way of remembering things
    # temporarily (like a sticky note)
    # get('cart', {}) = get the cart, or return empty {} if none

    cart_items = []
    # ↑ empty list — we'll fill it with product details
    
    total = 0
    # ↑ start total price at zero

    for product_id, quantity in cart.items():
        # ↑ loop through each item in the cart
        # product_id = the product's ID number
        # quantity = how many of that product

        try:
            product = Product.objects.get(id=product_id)
            # ↑ find that product in the database by its ID
            
            subtotal = product.price * quantity
            # ↑ calculate cost for this item
            
            total += subtotal
            # ↑ add to overall total
            
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })
            # ↑ add all info about this item to our list

        except Product.DoesNotExist:
            pass
            # ↑ if product not found, just skip it

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })
    # ↑ show cart page with items and total price


# ═══════════════════════════════
# VIEW 4 — Add to Cart
# ═══════════════════════════════
def add_to_cart(request, product_id):
    # product_id comes from the URL
    # like /add-to-cart/3/ means product number 3

    cart = request.session.get('cart', {})
    # ↑ get current cart (or empty one)

    product_id_str = str(product_id)
    # ↑ convert ID to string because session keys must be strings

    if product_id_str in cart:
        cart[product_id_str] += 1
        # ↑ if already in cart, just add 1 more
    else:
        cart[product_id_str] = 1
        # ↑ if new item, set quantity to 1

    request.session['cart'] = cart
    # ↑ save the updated cart back to the session
    # like putting the sticky note back on the fridge

    return redirect('cart')
    # ↑ send the user to the cart page


# ═══════════════════════════════
# VIEW 5 — Remove from Cart
# ═══════════════════════════════
def remove_from_cart(request, product_id):
    
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]
        # ↑ delete this item from the cart

    request.session['cart'] = cart
    # ↑ save updated cart

    return redirect('cart')
    # ↑ go back to cart page


# ═══════════════════════════════
# VIEW 6 — Order Form Page
# ═══════════════════════════════
def order_form(request):

    if request.method == 'POST':
        # ↑ POST means the user clicked the Submit button

        form = OrderForm(request.POST)
        # ↑ fill the form with what the user typed

        if form.is_valid():
            # ↑ check if everything was filled correctly

            form.save()
            # ↑ save the order to the database

            request.session['cart'] = {}
            # ↑ empty the cart after ordering
            # like cleaning the shopping basket

            return redirect('success')
            # ↑ send user to the success page

    else:
        form = OrderForm()
        # ↑ if user just visited the page (not submitted yet)
        # show them a blank form

    return render(request, 'store/order_form.html', {'form': form})
    # ↑ show the form page


# ═══════════════════════════════
# VIEW 7 — Success Page
# ═══════════════════════════════
def success(request):
    return render(request, 'store/success.html')
    # ↑ just show the success/thank you page