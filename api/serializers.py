# api/serializers.py (Versão Final Limpa e Organizada)

from rest_framework import serializers
from django.contrib.auth.models import User
# 1. TODOS os imports de models juntos e no topo!
from .models import UserProfile, DailyLog, MuscleGroup, Exercise, FoodCategory, FoodItem

# --- User & Profile Related ---

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

# --- Workout Related ---

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class MuscleGroupSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = MuscleGroup
        fields = ['id', 'name', 'exercises']

# --- Food Related ---

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class FoodCategorySerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ['id', 'name', 'food_items']