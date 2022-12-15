from django.contrib import admin

# Import the models that you want to register with the admin site
from .models import Product, Label, Cart

# Define a class for each model that you want to register
# with the admin site, that subclasses ModelAdmin
class ProductAdmin(admin.ModelAdmin):
    # Specify the fields and other attributes that you want
    # to display on the admin page for the Product model
    list_display = ('name', 'category', 'quantity', 'price')
    search_fields = ('name', 'category')

class LabelAdmin(admin.ModelAdmin):
    # Specify the fields and other attributes that you want
    # to display on the admin page for the Label model
    list_display = ('name',)

class CartAdmin(admin.ModelAdmin):
    # Specify the fields and other attributes that you want
    # to display on the admin page for the Cart model
    list_display = ('product', 'quantity')


# Register the models with the admin site by calling
# admin.site.register() for each model and passing in
# the model class and the corresponding ModelAdmin class
# as arguments
admin.site.register(Product, ProductAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Cart, CartAdmin)