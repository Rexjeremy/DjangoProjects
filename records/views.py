from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Transaction
from .forms import TransactionForm

def dashboard(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()

    transactions = Transaction.objects.all().order_by('-date')
    total_income = Transaction.objects.filter(transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    net_balance = total_income - total_expense

    context = {
        'form': form,
        'transactions': transactions,
        'income': total_income,
        'expense': total_expense,
        'balance': net_balance,
    }
    return render(request, 'dashboard.html', context)
