# gabgym_backend/api/serializers.py

from rest_framework import serializers
from .models import UserProfile, DailyLog
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    # AGORA, o campo 'user' é tratado de forma explícita.
    # Ele espera receber um ID (pk = Primary Key) e vai mostrar os dados do UserSerializer na leitura.
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    class Meta:
        model = UserProfile
        # Adicionamos 'user_id' nos campos para ele ser aceito na escrita
        fields = ['id', 'user', 'user_id', 'name', 'age', 'weight', 'height', 'gender', 'objective']

# O DailyLogSerializer continua igual por enquanto
class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'