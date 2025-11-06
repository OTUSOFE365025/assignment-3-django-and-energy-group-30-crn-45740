############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """
Product.objects.create(name='Banana', price=0.59, upc_code=4011)
Product.objects.create(name='Apple', price=0.99, upc_code=3099)
Product.objects.create(name='Carrot', price=1.19, upc_code=3011)
Product.objects.create(name='Onion', price=0.49, upc_code=2034)

quit = False
while quit == False:
    print("Enter a UPC code (or type Q to quit): ")
    code = input()
    if (code == "Q"):
        quit = True
        break
    else:
        for p in Product.objects.all(): #loop through all models in database
            try: #if the code is not a number or Q an error occurs when trying to cast code as an int
                if (int(code) == p.upc_code): #check if code is equal to each products upc code
                    code_found = True
                    break
                else:
                    code_found = False
            except:
                print("Please enter either an integer or Q")
                break

    if (code_found):
        print(f'Product: {p.name} \tPrice: {p.price} \tUPC code: {p.upc_code}') #if so, print product
    else:
        print("Code not found")
