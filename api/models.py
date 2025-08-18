# api/models.py (Versão Completa)

from django.db import models
from django.contrib.auth.models import User

# --- SEU CÓDIGO EXISTENTE (PERFEITO, NÃO MEXA) ---
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


# --- CÓDIGO NOVO (Adicionar no final do arquivo) ---
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
# --- FIM DO CÓDIGO NOVO ---