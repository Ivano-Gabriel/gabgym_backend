# gabgym_backend/gabgym_api/urls.py (Versão Corrigida)

from django.contrib import admin
from django.urls import path, include
# --- A LINHA QUE FALTAVA ESTÁ AQUI ---
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]

# Agora a condição "if settings.DEBUG" vai funcionar perfeitamente
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)