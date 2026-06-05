from django.shortcuts import render, redirect
from .models import SalesRecord
from .forms import SalesRecordForm
import json  # Added to safely parse data to the template layout

def dashboard(request):
    if request.method == 'POST':
        form = SalesRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SalesRecordForm()

    sales = SalesRecord.objects.all().order_by('-date', '-id')
    
    total_revenue = 0.0
    total_profit = 0.0
    
    # Chart dataset lists
    chart_labels = []
    chart_revenue = []
    chart_profit = []

    # Populate datasets (Taking the last 5 transactions to keep the mobile chart neat)
    for sale in reversed(list(sales[:5])):
        chart_labels.append(sale.item_name)
        chart_revenue.append(float(sale.total_revenue))
        chart_profit.append(float(sale.net_profit))
        
    for sale in sales:
        total_revenue += float(sale.total_revenue)
        total_profit += float(sale.net_profit)

    context = {
        'form': form,
        'sales': sales,
        'total_revenue': total_revenue,
        'total_profit': total_profit,
        # Safely convert Python lists into JSON strings for JavaScript to read
        'chart_labels': json.dumps(chart_labels),
        'chart_revenue': json.dumps(chart_revenue),
        'chart_profit': json.dumps(chart_profit),
    }
    return render(request, 'dashboard.html', context)
