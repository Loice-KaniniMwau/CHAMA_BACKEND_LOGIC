from django.db import models
from savingsgoals.models import SavingsGoals
from user.models import UserProfile

# Create your models here.

class Income(models.Model):
    # user=models.ForeignKey(Vendor,null=True,on_delete=models.CASCADE)
    user=models.ForeignKey(UserProfile,null=True,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)


class Expense(models.Model):
    user=models.ForeignKey(UserProfile,null=True,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
 

TRANSACTION_TYPE_CHOICES = (
    ("contribution", "Contribution"),
    ("withdrawal", "Withdrawal"),
)

class SavingsTransaction(models.Model):
    user=models.ForeignKey(UserProfile,null=True,on_delete=models.CASCADE)
    savingsgoals= models.ForeignKey(SavingsGoals,on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPE_CHOICES)


