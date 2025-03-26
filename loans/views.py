from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.utils import timezone
from .models import Loan
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            borrower = request.POST.get('borrower')
            amount = request.POST.get('amount')
            status = request.POST.get('status')
            due_date = request.POST.get('due_date') or None
            category = request.POST.get('category')
            if borrower and amount and status and category:
                Loan.objects.create(
                    user=request.user,  # Tied to logged-in user
                    borrower=borrower,
                    amount=amount,
                    status=status,
                    due_date=due_date,
                    category=category
                )
        elif 'delete' in request.POST:
            loan_id = request.POST.get('loan_id')
            loan = get_object_or_404(Loan, id=loan_id, user=request.user)  # Only user’s loans
            loan.delete()
        elif 'edit' in request.POST:
            loan_id = request.POST.get('loan_id')
            loan = get_object_or_404(Loan, id=loan_id, user=request.user)  # Only user’s loans
            loan.borrower = request.POST.get('borrower')
            loan.amount = request.POST.get('amount')
            loan.status = request.POST.get('status')
            loan.due_date = request.POST.get('due_date') or None
            loan.category = request.POST.get('category')
            loan.save()
        elif 'toggle' in request.POST:
            loan_id = request.POST.get('loan_id')
            loan = get_object_or_404(Loan, id=loan_id, user=request.user)  # Only user’s loans
            loan.status = 'Paid' if loan.status == 'Active' else 'Active'
            loan.save()
        return redirect('index')
    
    filter_status = request.GET.get('status', '')
    loans = Loan.objects.filter(user=request.user)  # Base filter by user
    if filter_status:
        loans = loans.filter(status=filter_status)  # Then apply status filter
    total_amount = loans.aggregate(models.Sum('amount'))['amount__sum'] or 0
    active_total = loans.filter(status='Active').aggregate(models.Sum('amount'))['amount__sum'] or 0
    paid_total = loans.filter(status='Paid').aggregate(models.Sum('amount'))['amount__sum'] or 0
    overdue = loans.filter(status='Active', due_date__lt=timezone.now().date()).count()
    chart_data = {
        'active': float(active_total),
        'paid': float(paid_total)
    }
    return render(request, 'loans/index.html', {
        'loans': loans,
        'filter_status': filter_status,
        'total_amount': total_amount,
        'active_total': active_total,
        'paid_total': paid_total,
        'overdue': overdue,
        'today': timezone.now().date(),
        'chart_data': chart_data
    })