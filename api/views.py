# api/views.py

from rest_framework import viewsets, permissions
from .models import UserProfile, DailyLog
from .serializers import UserProfileSerializer, DailyLogSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Garante que um usuário só possa ver/editar o seu próprio perfil
        return UserProfile.objects.filter(user=self.request.user)

class DailyLogViewSet(viewsets.ModelViewSet):
    serializer_class = DailyLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Garante que um usuário só possa ver os seus próprios registros do diário
        try:
            user_profile = UserProfile.objects.get(user=self.request.user)
            return DailyLog.objects.filter(user_profile=user_profile)
        except UserProfile.DoesNotExist:
            return DailyLog.objects.none() # Retorna uma lista vazia se o perfil não existir

    def perform_create(self, serializer):
        # Garante que um novo registro seja associado ao perfil do usuário logado
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer.save(user_profile=user_profile)
        
# api/views.py (Versão Completa)

from rest_framework import viewsets, permissions
# Importamos os novos modelos e serializers
from .models import UserProfile, DailyLog, MuscleGroup, Exercise
from .serializers import UserProfileSerializer, DailyLogSerializer, MuscleGroupSerializer, ExerciseSerializer

# --- SEU CÓDIGO EXISTENTE (PERFEITO, NÃO MEXA) ---
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Garante que um usuário só possa ver/editar o seu próprio perfil
        return UserProfile.objects.filter(user=self.request.user)

class DailyLogViewSet(viewsets.ModelViewSet):
    serializer_class = DailyLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Garante que um usuário só possa ver os seus próprios registros do diário
        try:
            user_profile = UserProfile.objects.get(user=self.request.user)
            return DailyLog.objects.filter(user_profile=user_profile)
        except UserProfile.DoesNotExist:
            return DailyLog.objects.none() # Retorna uma lista vazia se o perfil não existir

    def perform_create(self, serializer):
        # Garante que um novo registro seja associado ao perfil do usuário logado
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer.save(user_profile=user_profile)
# --- FIM DO SEU CÓDIGO EXISTENTE ---


# --- CÓDIGO NOVO (Adicionar no final do arquivo) ---
# Usamos ReadOnly porque, por enquanto, o frontend só precisa LER esses dados
class MuscleGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer
    # Deixamos sem permissão para qualquer um poder ver a lista de exercícios
    permission_classes = [permissions.AllowAny] 

class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.AllowAny]
# --- FIM DO CÓDIGO NOVO ---