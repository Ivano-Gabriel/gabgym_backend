# api/serializers.py

from rest_framework import serializers
from .models import UserProfile, DailyLog
from django.contrib.auth.models import User

# Serializer para mostrar informações básicas do usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer para o Perfil do Usuário
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) # Mostra os dados do usuário, em vez de só o ID

    class Meta:
        model = UserProfile
        fields = '__all__'

# Serializer para o Diário de Bordo
class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'
        
# api/serializers.py (Versão Completa)

from rest_framework import serializers
from .models import UserProfile, DailyLog, MuscleGroup, Exercise # Importamos os novos modelos
from django.contrib.auth.models import User

# --- SEU CÓDIGO EXISTENTE (PERFEITO, NÃO MEXA) ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'

class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'
# --- FIM DO SEU CÓDIGO EXISTENTE ---


# --- CÓDIGO NOVO (Adicionar no final do arquivo) ---
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class MuscleGroupSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = MuscleGroup
        fields = ['id', 'name', 'exercises']
# --- FIM DO CÓDIGO NOVO ---