from django.db import models
from django.utils import timezone

class SalesRecord(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('TRANSFER', 'Bank Transfer'),
        ('POS', 'POS Terminal'),
        ('CREDIT', 'Customer Credit / Owing'),
    ]

    date = models.DateField(default=timezone.now)
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    cost_price_per_item = models.DecimalField(max_digits=12, decimal_places=2)
    selling_price_per_item = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='TRANSFER')
    customer_name = models.CharField(max_length=150, blank=True, null=True)

    @property
    def total_revenue(self):
        return self.selling_price_per_item * self.quantity

    @property
    def total_cost(self):
        return self.cost_price_per_item * self.quantity

    @property
    def net_profit(self):
        return self.total_revenue - self.total_cost

    def __str__(self):
        return f"{self.item_name} ({self.quantity}) - Rev: ₦{self.total_revenue}"
