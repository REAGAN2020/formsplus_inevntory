
from django.urls import path
from .views import Product,Cart, Label,LabelSerializer,ProductSerializer,LabelSerializer
from . import views


urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('purchase/', views.PurchaseView.as_view(), name='purchase'),
]


