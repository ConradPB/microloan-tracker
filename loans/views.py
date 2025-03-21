from django.shortcuts import render
from .models import Loan

def index(request):
    loans = Loan.objects.all()
    return render(request, 'loans/index.html', {'loans': loans})
