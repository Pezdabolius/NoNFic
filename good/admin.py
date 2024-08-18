from django.contrib import admin
from .models import Product, Category, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'information',
                    'available','price', 'update',
                    'create']
    search_fields = ['name']
    list_filter = ['available']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'title', 'body', 'created']