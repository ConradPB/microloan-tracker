from django.shortcuts import render, redirect, get_object_or_404
from .models import Loan

def index(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            borrower = request.POST.get('borrower')
            amount = request.POST.get('amount')
            status = request.POST.get('status')
            if borrower and amount and status:
                Loan.objects.create(borrower=borrower, amount=amount, status=status)
        elif 'delete' in request.POST:
            loan_id = request.POST.get('loan_id')
            loan = get_object_or_404(Loan, id=loan_id)
            loan.delete()
        elif 'edit' in request.POST:
            loan_id = request.POST.get('loan_id')
            loan = get_object_or_404(Loan, id=loan_id)
            loan.borrower = request.POST.get('borrower')
            loan.amount = request.POST.get('amount')
            loan.status = request.POST.get('status')
            loan.save()
        return redirect('index')
    
    filter_status = request.GET.get('status', '')
    loans = Loan.objects.filter(status=filter_status) if filter_status else Loan.objects.all()
    total_amount = loans.aggregate(models.Sum('amount'))['amount__sum'] or 0
    return render(request, 'loans/index.html', {
        'loans': loans,
        'filter_status': filter_status,
        'total_amount': total_amount
    })