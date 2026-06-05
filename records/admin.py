from django.contrib import admin
from .models import SalesRecord

@admin.register(SalesRecord)
class SalesRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'item_name', 'quantity', 'selling_price_per_item', 'payment_method', 'customer_name')
    list_filter = ('payment_method', 'date')
    search_fields = ('item_name', 'customer_name')
