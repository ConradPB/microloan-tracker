from django.db import models

from django.db import models

class Loan(models.Model):
    borrower = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.borrower} - ${self.amount}"
