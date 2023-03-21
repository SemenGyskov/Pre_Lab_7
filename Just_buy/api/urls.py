from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cart-add/', CartCreate.as_view(), name='cart-add'),
    path('cart/', CartList.as_view(), name='cart_list'),
    path('cart/<int:pk>/', CartAPIUpdate.as_view(), name='cart_update'),
    path('order/', OrderList.as_view(), name='order_list'),
    path('order-add/', OrderCreate.as_view(), name='order-add'),
    path('order/<int:pk>/', OrderAPIUpdate.as_view(), name='order_update'),
    path('product/', ProductList.as_view(), name='product_list'),
    path('product-add/', ProductCreate.as_view(), name='product_add'),
    path('product/<int:pk>/', ProductAPIUpdate.as_view(), name='product_update'),
    path('auth/', include('rest_framework.urls')),

]