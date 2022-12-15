
from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    LabelListCreateAPIView,
    LabelRetrieveUpdateDestroyAPIView,
    CartListView,
    CartDetailView
)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('labels/', LabelListCreateAPIView.as_view(), name='label-list-create'),
    path('labels/<int:pk>', LabelRetrieveUpdateDestroyAPIView.as_view(), name='label-retrieve-update-destroy'),
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<int:pk>', CartDetailView.as_view(), name='cart-detail')
]