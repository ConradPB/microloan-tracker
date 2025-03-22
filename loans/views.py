from django.shortcuts import render, redirect
from .models import Loan

def index(request):
    if request.method == 'POST':
        borrower = request.POST.get('borrower')
        amount = request.POST.get('amount')
        status = request.POST.get('status')
        if borrower and amount and status:
            Loan.objects.create(borrower=borrower, amount=amount, status=status)
        return redirect('index')
    filter_status = request.GET.get('status', '')
    loans = Loan.objects.filter(status=filter_status) if filter_status else Loan.objects.all()
    return render(request, 'loans/index.html', {'loans': loans, 'filter_status': filter_status})