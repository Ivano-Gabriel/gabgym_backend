# gabgym_backend/api/admin.py

from django.contrib import admin
from .models import UserProfile, DailyLog # Importa nossos modelos

# Registra os modelos para que eles apareçam no painel de admin
admin.site.register(UserProfile)
admin.site.register(DailyLog)