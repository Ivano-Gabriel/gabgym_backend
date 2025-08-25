# gabgym_backend/api/urls.py (Versão Final e Correta)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
# 1. Importamos SOMENTE os ViewSets que nós criamos
from .views import MuscleGroupViewSet, ExerciseViewSet, FoodCategoryViewSet

# 2. Criamos o nosso roteador automático
router = DefaultRouter()

# 3. Registramos cada rota com seu respectivo ViewSet
router.register(r'muscle-groups', MuscleGroupViewSet, basename='musclegroup')
router.register(r'exercises', ExerciseViewSet, basename='exercise') # A rota de exercícios que faltava
router.register(r'food-categories', FoodCategoryViewSet, basename='foodcategory')

# 4. Incluímos todas as URLs geradas pelo roteador
urlpatterns = [
    path('', include(router.urls)),
]