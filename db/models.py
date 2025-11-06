import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    upc_code = models.IntegerField(unique=True)
    def __str__(self):
        return self.product, self.price, self.upc_code
