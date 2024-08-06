from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_list_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    information = models.TextField(max_length=500, blank=True)
    description = models.TextField(max_length=1200)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField()
    count_reviews = models.PositiveIntegerField(default=0, blank=True)
    count_sold = models.PositiveIntegerField(default=0, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']