from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'transaction_type', 'amount', 'category')
    list_filter = ('transaction_type', 'category', 'date')
    search_fields = ('title', 'description', 'category')

