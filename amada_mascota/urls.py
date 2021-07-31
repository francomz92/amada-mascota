from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('', include('apps.urls')),
    path('', include('apps.usuario.urls')),
    path('', include('apps.adopcion.urls')),
    path('', include('apps.encontrados.urls')),
    path('', include('apps.perdidos.urls')),
    path('', include('apps.suscripcion.urls')),
    path('', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)