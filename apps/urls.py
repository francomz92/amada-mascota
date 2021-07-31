from apps.views import PrivateDeletePublicacion, PrivateRenovatePublicacion
from django.urls import path

app_name = 'apps'

urlpatterns = [
    path(
        'renovar-publicacion/<int:id>/',
        PrivateRenovatePublicacion.as_view(),
        name='private_renovate_publicacion',
    ),
    path(
        'borrar-publicacion/<int:id>/',
        PrivateDeletePublicacion.as_view(),
        name='private_delete_publicacion',
    ),
]