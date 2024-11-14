from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    name = models.CharField(max_length=221)
    description = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()

class Email(models.Model):
    email = models.EmailField()
