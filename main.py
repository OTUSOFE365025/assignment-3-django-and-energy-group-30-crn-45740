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

from tkinter import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

def scanUPCCODE():
    code_found = False
    for p in Product.objects.all(): #loop through all models in database
        try: #if the code is not a number error occurs when trying to cast the code as an int
            if (int(user_code.get()) == p.upc_code): #check if code is equal to each products upc code
                code_found = True
                break
            else:
                code_found = False
        except:
            break

    if (code_found):
        product_info = f"Product: {p.name} | Price: ${p.price} | UPC code: {p.upc_code}"
        return_code.config(text = product_info)
    else:
        return_code.config(text = "Code not found")

#add sample products to database
Product.objects.create(name='Banana', price=0.59, upc_code=4011)
Product.objects.create(name='Apple', price=0.99, upc_code=3099)
Product.objects.create(name='Carrot', price=1.19, upc_code=3011)
Product.objects.create(name='Onion', price=0.49, upc_code=2034)

window = Tk() #create window
window.geometry("350x100") #set dimensions of window
window.title('Cash Register Scanner')

return_code = Label(window) #create text box to display product info
return_code.pack()

user_code = Entry(window) #create input box
user_code.focus() #set focus to input box on start up
user_code.pack()

button = Button(window, text = "Submit", width = 20, command = scanUPCCODE) #create button that runs scanUPCCODE function when clicked
button.pack()

window.mainloop()
