from django.db import models

class Loan(models.Model):
    borrower = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Paid', 'Paid')], default='Active')
    category = models.CharField(max_length=20, choices=[('Personal', 'Personal'), ('Business', 'Business')], default='Personal')

    def __str__(self):
        return f"{self.borrower} - ${self.amount} ({self.status})"