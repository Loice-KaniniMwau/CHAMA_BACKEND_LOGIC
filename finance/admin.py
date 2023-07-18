from django.contrib import admin
from .models import Saving, SavingContribution, MeriGoRoundContribution

# Register your models with the admin interface

class SavingAdmin(admin.ModelAdmin):
    list_display = ('year', 'amount_saved', 'interest_earned', 'total_savings')

class SavingContributionAdmin(admin.ModelAdmin):
    list_display = ('saving', 'amount', 'created')

class MeriGoRoundContributionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'status', 'created', 'updated')

admin.site.register(Saving, SavingAdmin)
admin.site.register(SavingContribution, SavingContributionAdmin)
admin.site.register(MeriGoRoundContribution, MeriGoRoundContributionAdmin)

