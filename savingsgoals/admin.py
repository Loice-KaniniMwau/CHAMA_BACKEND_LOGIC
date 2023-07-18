from django.contrib import admin
from .models import SavingsGoals

class SavingsGoalsAdmin(admin.ModelAdmin):
    list_display=('title','target_amount','due_date','progress','notes','category','alert','created_at','updated_at')

admin.site.register(SavingsGoals,SavingsGoalsAdmin)


