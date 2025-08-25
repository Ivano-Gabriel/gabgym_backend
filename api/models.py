# api/models.py (Versão Completa)

from django.db import models
from django.contrib.auth.models import User

# --- S
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    objective = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

class DailyLog(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField(auto_now_add=True)
    calories_consumed = models.IntegerField(default=0)
    protein_consumed = models.IntegerField(default=0)
    carbs_consumed = models.IntegerField(default=0)
    fat_consumed = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Log for {self.user_profile.user.username} on {self.date}"
# --- FIM DO SEU CÓDIGO EXISTENTE ---

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    local_video_path = models.CharField(max_length=255, blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    muscle_group = models.ForeignKey(MuscleGroup, related_name='exercises', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class FoodCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50, blank=True)
    serving_desc = models.CharField(max_length=100, blank=True)
    calories = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    image_path = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(FoodCategory, related_name='food_items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name