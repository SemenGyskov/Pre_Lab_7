from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    title = models.CharField(max_length=100, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Cart(models.Model):
    products = models.ManyToManyField(Product, verbose_name='Продукт')
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class Order(models.Model):
    products = models.ManyToManyField(Cart, verbose_name='Продукты')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая Стоимость Заказа')
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'