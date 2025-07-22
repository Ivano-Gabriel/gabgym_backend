# gabgym_backend/api/models.py

from django.db import models
from django.contrib.auth.models import User

# Modelo para guardar os dados do perfil do usuário, ligado ao sistema de usuários do Django
class UserProfile(models.Model):
    # Relação um-para-um: cada Usuário do Django tem apenas um Perfil
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Campos que vêm do nosso formulário do React
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    
    # Usamos choices para limitar as opções, o que é uma boa prática
    GENDER_CHOICES = [
        ('male', 'Masculino'),
        ('female', 'Feminino'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    
    OBJECTIVE_CHOICES = [
        ('lose-fat', 'Perder Gordura'),
        ('maintain', 'Manter Peso'),
        ('gain-muscle', 'Ganhar Massa'),
    ]
    objective = models.CharField(max_length=12, choices=OBJECTIVE_CHOICES)

    def __str__(self):
        return self.user.username


# Modelo para guardar cada registro diário do usuário
class DailyLog(models.Model):
    # Relação muitos-para-um: cada Usuário pode ter muitos registros no diário
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    # A data em que o registro foi feito
    date = models.DateField(auto_now_add=True)
    
    # O tipo de registro que estamos salvando
    LOG_TYPE_CHOICES = [
        ('food', 'Comida'),
        ('exercise', 'Exercício'),
        ('water', 'Água'),
        ('sleep', 'Sono'),
    ]
    log_type = models.CharField(max_length=10, choices=LOG_TYPE_CHOICES)
    
    # Detalhes do registro
    name = models.CharField(max_length=100) # Ex: "Maçã", "Corrida Moderada", "Sono"
    calories = models.FloatField(null=True, blank=True) # Pode ser nulo para água/sono
    protein = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    volume_ml = models.IntegerField(null=True, blank=True) # Específico para água
    duration_minutes = models.IntegerField(null=True, blank=True) # Específico para sono/exercício

    def __str__(self):
        return f'{self.user_profile.user.username} - {self.name} em {self.date}'