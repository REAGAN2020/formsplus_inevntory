from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductSerializer, CartSerializer, LabelSerializer
from .models import Product, Cart, Label


# Create your views here.

# Retrieve a list of all products
def get_products(request):
    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())})

# Create a new product
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        labels = request.POST.get('labels')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        product = Product(name=name, category=category, quantity=quantity, price=price)
        product.save()

        for label in labels:
            product.labels.add(label)

        return JsonResponse({'product': product.id})

# Update an existing product
@csrf_exempt
def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'PUT':
        name = request.POST.get('name')
        category = request.POST.get('category')
        labels = request.POST.get('labels')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        product.name = name
        product.category = category
        product.quantity = quantity
        product.price = price
        product.save()

        product.labels.set(labels)

        return JsonResponse({'product': product.id})

# Delete an existing product
@csrf_exempt
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)

# Retrieve a single product by its ID
def get_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return JsonResponse({'product': {
        'name': product.name,
        'category': product.category,
        'labels': list(product.labels.values()),
        'quantity': product.quantity,
        'price': product.price
    }})

# Add a product to the user's cart
@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        # Retrieve the product with the specified id
        product = get_object_or_404(Product, pk=product_id)

        # Create a new Cart object with the product and quantity
        cart = Cart(product=product, quantity=quantity)

        # Save the object to the database
        cart.save()

        return HttpResponse('Product added to cart')
    

# def purchase(request):
#     if request.method == 'POST':
#         # Retrieve all items in the cart
#         cart_items = Cart.objects.all()

#         # Process the purchase by updating the product quantities and removing the items from the cart
#         for item in cart_items:
#             product = item.product
#             product.quantity -= item.quantity
#             product.save()
#             item.delete()

#         return HttpResponse('Purchase successful')

@csrf_exempt
def purchase(request):
    if request.method == 'POST':
        # Retrieve the user's cart from the database
        cart = Cart.objects.all()

        # Iterate over the products in the cart
        for item in cart:
            product = item.product
            quantity = item.quantity

            # Decrement the product's quantity by the corresponding cart quantity
            product.quantity -= quantity

            # If the product's quantity becomes zero or negative, delete it from the database
            if product.quantity <= 0:
                product.delete()
            else:
                # Otherwise, save the updated product to the database
                product.save()

        # Clear the cart
        cart.delete()

        return HttpResponse('Purchase successful')