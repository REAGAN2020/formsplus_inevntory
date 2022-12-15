from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer, LabelSerializer, CartSerializer
from .models import Product, Label, Cart


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def post(self, request, *args, **kwargs):
        # Get the user's cart
        cart = self.get_cart(request)

        # Get the product to add to the cart
        product = self.get_object()

        # Add the product to the cart
        cart.add_product(product)

        # Return the updated cart
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def put(self, request, *args, **kwargs):
        # Get the user's cart
        cart = self.get_cart(request)

        # Get the product to update in the cart
        product = self.get_object()

        # Update the product in the cart
        cart.update_product(product)

        # Return the updated cart
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        # Get the user's cart
        cart = self.get_cart(request)

        # Get the product to remove from the cart
        product = self.get_object()

        # Remove the product from the cart
        cart.remove_product(product)

        # Return the updated cart
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

class LabelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class LabelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def post(self, request, *args, **kwargs):
        # Get the user's cart
        cart = self.get_cart(request)

        # Purchase the products in the cart
        cart.purchase()

        # Return the updated cart
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer