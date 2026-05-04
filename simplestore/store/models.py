from django.db import models

# A Model is like a table in Excel
# This one stores all our products

class Product(models.Model):
    # Each line below is one column in our table

    name = models.CharField(max_length=200)
    # ↑ stores the product name (like "Blue Sneakers")
    # max_length=200 means maximum 200 letters

    description = models.TextField()
    # ↑ stores a longer description of the product

    price = models.DecimalField(max_digits=10, decimal_places=2)
    # ↑ stores the price (like 25.99)
    # decimal_places=2 means two numbers after the dot

    image_url = models.URLField(blank=True)
    # ↑ stores a link to the product image
    # blank=True means this field is optional

    def __str__(self):
        return self.name
        # ↑ this makes Django show the product NAME
        # instead of "Product object (1)" in the admin panel


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


# ═══════════════════════════════
# NEW — Order Model
# ═══════════════════════════════
class Order(models.Model):
    name = models.CharField(max_length=200)
    # ↑ customer's full name

    phone = models.CharField(max_length=20)
    # ↑ customer's phone number

    address = models.TextField()
    # ↑ delivery address

    created_at = models.DateTimeField(auto_now_add=True)
    # ↑ automatically saves the date and time
    # when the order was placed
    # auto_now_add=True means "save the time RIGHT NOW
    # and never change it"

    def __str__(self):
        return f"Order by {self.name} on {self.created_at}"
        # ↑ shows something like:
        # "Order by Takudzwa on 2024-01-15 10:30"