from django.contrib import admin
from .models import Category, Food , User

# Register your models here.
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(User)
