# gabgym_backend/api/views.py

from rest_framework import viewsets, permissions
from .models import UserProfile, DailyLog
from .serializers import UserProfileSerializer, DailyLogSerializer

# Nossos novos imports para o login social
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

# A View que vai fazer a "troca" do token do Google pelo nosso token
class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    

# Nossas views de dados continuam aqui
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # A permissão aqui será trocada no futuro para IsAuthenticated
    permission_classes = [permissions.AllowAny] 
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user__id=user_id)
        return queryset

class DailyLogViewSet(viewsets.ModelViewSet):
    queryset = DailyLog.objects.all()
    serializer_class = DailyLogSerializer
    permission_classes = [permissions.AllowAny]