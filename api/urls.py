# api/urls.py (Versão Completa)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Importamos as novas Views
from .views import UserProfileViewSet, DailyLogViewSet, MuscleGroupViewSet, ExerciseViewSet

router = DefaultRouter()
# Rotas que você já tinha
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile') 
router.register(r'dailylogs', DailyLogViewSet, basename='dailylog')

# --- CÓDIGO NOVO ---
# Adicionando as novas rotas ao mesmo roteador
router.register(r'muscle-groups', MuscleGroupViewSet, basename='musclegroup')
router.register(r'exercises', ExerciseViewSet, basename='exercise')
# --- FIM DO CÓDIGO NOVO ---

urlpatterns = [
    path('', include(router.urls)),
]