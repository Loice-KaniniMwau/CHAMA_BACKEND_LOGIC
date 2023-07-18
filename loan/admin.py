from django.contrib import admin
from .models import LoanApplication, Loan, LoanGuarantor, LoanPayment

# Register your models with the admin interface

class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('loan_type', 'amount_applying', 'created_at', 'status')
   

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_application', 'loan_type', 'amount_awarded', 'amount_to_repay', 'status')
    # search_fields = ('user__username', 'loan_application__loan_type', 'amount_awarded', 'amount_to_repay')
    # list_filter = ('status', 'loan_type')

class LoanGuarantorAdmin(admin.ModelAdmin):
    list_display = ('name', 'loan', 'relationship', 'created_at')
    # search_fields = ('User__username', 'name', 'loan__loan_type')
    # list_filter = ('relationship',)

class LoanPaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'amount', 'payment_method', 'date_paid')
    # search_fields = ('User__username', 'loan__loan_type', 'amount', 'payment_method')
    # list_filter = ('payment_method',)

admin.site.register(LoanApplication, LoanApplicationAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(LoanGuarantor, LoanGuarantorAdmin)
admin.site.register(LoanPayment, LoanPaymentAdmin)
