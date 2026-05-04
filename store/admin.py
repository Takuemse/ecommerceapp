from django.contrib import admin
from .models import Product
# ↑ we're importing our Product model

admin.site.register(Product)
# ↑ this adds Product to the admin panel
# so we can add/edit/delete products easily

from django.contrib import admin
from .models import Product, Order
# ↑ import both models

admin.site.register(Order)
# ↑ add both to admin panel