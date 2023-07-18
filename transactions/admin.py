from django.contrib import admin
from .models import Income,Expense,SavingsTransaction
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount','date','description')

@admin.register(Expense)    
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount','date','description','category')
    

@admin.register(SavingsTransaction)
class SavingsTransactionAdmin(admin.ModelAdmin):
    list_display=('savingsgoals','amount','date','description','transaction_type')


 




