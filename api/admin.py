# api/admin.py (Versão Completa)
from django.contrib import admin
from .models import UserProfile, DailyLog, MuscleGroup, Exercise # Importamos TODOS os modelos

# Registrando os modelos que já existiam
admin.site.register(UserProfile)
admin.site.register(DailyLog)

# --- CÓDIGO NOVO ---
# Registrando os novos modelos para aparecerem no Admin
admin.site.register(MuscleGroup)
admin.site.register(Exercise)
# --- FIM DO CÓDIGO NOVO ---