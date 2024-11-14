from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=221)
    description = models.TextField()
    image = models.ImageField(upload_to='shop_image/')
    price = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

