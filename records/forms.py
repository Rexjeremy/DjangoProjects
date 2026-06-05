from django import forms
from .models import SalesRecord

class SalesRecordForm(forms.ModelForm):
    class Meta:
        model = SalesRecord
        fields = ['date', 'item_name', 'quantity', 'cost_price_per_item', 'selling_price_per_item', 'payment_method', 'customer_name']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
