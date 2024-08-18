from django.contrib import admin
from .models import Order, CartOrder


class CartOrderInline(admin.TabularInline):
    model = CartOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'country',
                    'city', 'address', 'postal_code', 'paid']
    list_filter = ['paid']
    list_editable = ['paid']
    inlines = [CartOrderInline,]


admin.site.register(Order, OrderAdmin)
