from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    labels = models.ManyToManyField('Label')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Label(models.Model):
    name = models.CharField(max_length=255)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()