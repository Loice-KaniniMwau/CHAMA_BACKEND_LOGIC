from django.contrib import admin
# myapp/admin.py

from .models import UserProfile, Employment, Education, MpesaDetail, FamilyMember

# Register your models with the admin interface

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'gender_status', 'marital_status')
    list_filter = ('gender_status', 'marital_status')
    # search_fields = ('user__username', 'id_number', 'phone_number')

@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('employment_status', 'employer', 'date_employed')
    list_filter = ('employment_status', 'employer')
    # search_fields = ('user__user__username', 'employer')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('highest_education_level', 'last_school_attended', 'year_joined', 'graduation_year')
    list_filter = ('highest_education_level', 'year_joined', 'graduation_year')
    # search_fields = ('user__user__username', 'last_school_attended')

@admin.register(MpesaDetail)
class MpesaDetailAdmin(admin.ModelAdmin):
    list_display = ('payment_method', 'mpesa_number', 'preferred_payment_day')
    list_filter = ('payment_method', 'preferred_payment_day')
    # search_fields = ('user__user__username', 'mpesa_number')

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'relationship', 'gender', 'marital_status')
    list_filter = ('relationship', 'gender', 'marital_status')
    # search_fields = ('user__user__username', 'name', 'phone_number', 'email')

