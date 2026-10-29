from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.category_name
    
    
class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_quantity = models.IntegerField(max_length=50)
    item_image = models.ImageField(upload_to='food_images/', null=True, blank=True)
    item_description = models.TextField(max_length=500)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item_name} ({self.category.category_name})"