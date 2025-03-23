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
        