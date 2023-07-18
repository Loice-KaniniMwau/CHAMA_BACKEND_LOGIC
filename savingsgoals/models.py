from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile
# Create your models here.
class SavingsGoals(models.Model):
    GOAL_CATEGORY=(("financial","Financial"),("personal","Personal"),)
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    target_amount=models.DecimalField(max_digits=255,decimal_places=2)
    due_date=models.DateField()
    progress=models.TextField()
    notes=models.TextField()
    category=models.CharField(max_length=255,choices=GOAL_CATEGORY)
    alert=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
