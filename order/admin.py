from django.contrib import admin
from order.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'time', 'amount', 'dispatched', 'delivered', 'paid']
    search_fields = ['user']

admin.site.register(Order, OrderAdmin)