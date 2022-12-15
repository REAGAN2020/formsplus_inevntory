"""inventory_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from api.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, LabelListCreateAPIView, LabelRetrieveUpdateDestroyAPIView, CartListView, CartDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('labels/', LabelListCreateAPIView.as_view(), name='label-list-create'),
    path('labels/<pk>', LabelRetrieveUpdateDestroyAPIView.as_view(), name='label-retrieve-update-destroy'),
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<pk>', CartDetailView.as_view(), name='cart-detail')
]
