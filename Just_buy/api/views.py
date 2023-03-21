from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import *

class CartCreate(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
class CartList(APIView):
    def get(self,request):
        w = Cart.objects.all()
        return Response({'Carts':CartSerializer(w,many=True).data})
    permission_classes = (IsAuthenticated,)

class CartAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminUser,)

class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

class OrderList(APIView):
    def get(self, request):
        w = Order.objects.all()
        return Response({'Orders': OrderSerializer(w, many=True).data})
    permission_classes = (IsAuthenticated,)

class OrderAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)

class ProductList(APIView):
    def get(self, request):
        w = Product.objects.all()
        return Response({'Items': ProductSerializer(w, many=True).data})
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ProductAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)

