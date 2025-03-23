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
            category = request.POST.get('category')
            if borrower and amount and status and category:
                Loan.objects.create(borrower=borrower, amount=amount, status=status, due_date=due_date, category=category)
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
            loan.category = request.POST.get('category')
            loan.save()
        elif 'toggle' in request.POST:
            loan_id = request.POST.get('loan_id')
            loan = get_object_or_404(Loan, id=loan_id)
            loan.status = 'Paid' if loan.status == 'Active' else 'Active'
            loan.save()
        return redirect('index')
    
    