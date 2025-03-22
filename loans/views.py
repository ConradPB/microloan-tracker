from django.shortcuts import render, redirect
from .models import Loan

def index(request):
    if request.method == 'POST':
        borrower = request.POST.get('borrower')
        amount = request.POST.get('amount')
        if borrower and amount:
            Loan.objects.create(borrower=borrower, amount=amount)
        return redirect('index')
    loans = Loan.objects.all()
    return render(request, 'loans/index.html', {'loans': loans})