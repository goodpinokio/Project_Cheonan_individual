from django.contrib import admin
from .models import Shop, Item, Order

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'addr')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('shop', 'name', 'price')
    list_filter = ('shop',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('shop', 'user', 'created_at')
    list_filter = ('shop', 'user')

admin.site.register(Shop, ShopAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)