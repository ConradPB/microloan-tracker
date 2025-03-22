from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.utils import timezone
from .models import Loan

def index(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            borrower = request.POST.get('borrower')
            amount = request.POST.get('amount')
            status = request.POST.get('status')
            due_date = request.POST.get('due_date') or None
            if borrower and amount and status:
                Loan.objects.create(borrower=borrower, amount=amount, status=status, due_date=due_date)
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
            loan.due_date = request.POST.get('due_date') or None
            loan.save()
        elif 'toggle' in request.POST:
            loan_id = request.POST.get('loan_id')
            loan = get_object_or_404(Loan, id=loan_id)
            loan.status = 'Paid' if loan.status == 'Active' else 'Active'
            loan.save()
        return redirect('index')
    
    filter_status = request.GET.get('status', '')
    loans = Loan.objects.filter(status=filter_status) if filter_status else Loan.objects.all()
    total_amount = loans.aggregate(models.Sum('amount'))['amount__sum'] or 0
    active_total = Loan.objects.filter(status='Active').aggregate(models.Sum('amount'))['amount__sum'] or 0
    paid_total = Loan.objects.filter(status='Paid').aggregate(models.Sum('amount'))['amount__sum'] or 0
    overdue = Loan.objects.filter(status='Active', due_date__lt=timezone.now().date()).count()
    return render(request, 'loans/index.html', {
        'loans': loans,
        'filter_status': filter_status,
        'total_amount': total_amount,
        'active_total': active_total,
        'paid_total': paid_total,
        'overdue': overdue
    })