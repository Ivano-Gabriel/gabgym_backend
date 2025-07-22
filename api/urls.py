# gabgym_backend/api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, DailyLogViewSet

# O Router que já conhecemos
router = DefaultRouter()
# Adicionei o basename de volta para garantir que não teremos erros futuros
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile') 
router.register(r'dailylogs', DailyLogViewSet)

# As URLs da nossa API de dados
urlpatterns = [
    path('', include(router.urls)),
]