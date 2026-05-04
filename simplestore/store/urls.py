from django.urls import path
from . import views
# ↑ import all our views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # ↑ empty string = homepage = http://127.0.0.1:8000/

    path('products/', views.product_list, name='product_list'),
    # ↑ http://127.0.0.1:8000/products/

    path('cart/', views.cart, name='cart'),
    # ↑ http://127.0.0.1:8000/cart/

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # ↑ <int:product_id> = a number in the URL
    # like /add-to-cart/3/ means product ID 3

    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # ↑ http://127.0.0.1:8000/remove/3/

    path('order/', views.order_form, name='order_form'),
    # ↑ http://127.0.0.1:8000/order/

    path('success/', views.success, name='success'),
    # ↑ http://127.0.0.1:8000/success/
]