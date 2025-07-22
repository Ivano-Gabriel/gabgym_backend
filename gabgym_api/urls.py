# gabgym_backend/gabgym_api/urls.py

from django.contrib import admin
from django.urls import path, include
from api.views import GoogleLoginView # Importa nossa nova view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Nossas rotas da API de dados (perfis, logs, etc)
    path('api/', include('api.urls')),
    
    # A ROTA DA NOSSA "CASA DE CÂMBIO"
    path('api/auth/google/', GoogleLoginView.as_view(), name='google_login'),
    
    # Rotas de autenticação padrão (logout, etc.) que o dj-rest-auth provê
    path('api/auth/', include('dj_rest_auth.urls')),
    
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]