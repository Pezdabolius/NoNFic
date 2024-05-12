from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description',
                    'available', 'price',
                    'update', 'create']
    list_filter = ['available']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug': ['name']}