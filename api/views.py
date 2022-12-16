from django.shortcuts import render
from django.http import JsonResponse
from .serializers import ProductSerializer, LabelSerializer, CartSerializer
from .models import Product, Label, Cart

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_list = [{'name': product.name, 'category': product.category, 'labels': [label.name for label in product.labels.all()], 'quantity': product.quantity, 'price': str(product.price)} for product in products]
        return JsonResponse({'products': products_list})
    elif request.method == 'POST':
        data = request.POST
        name = data.get('name')
        category = data.get('category')
        labels = data.get('labels')
        quantity = data.get('quantity')
        price = data.get('price')
        product = Product.objects.create(name=name, category=category, quantity=quantity, price=price)
        product.labels.set(labels)
        product.save()
        return JsonResponse({'message': 'Product created successfully.'})