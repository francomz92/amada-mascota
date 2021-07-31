from django.urls import path
from .views import PrivateDeleteSuscripcion, PrivateSuscripciones

app_name = 'suscripcion'

urlpatterns = [
    path(
        'suscripciones/',
        PrivateSuscripciones.as_view(),
        name='private_suscripcion',
    ),
    path(
        'borrar-suscripcion/<int:id>/',
        PrivateDeleteSuscripcion.as_view(),
        name='private_delete_suscripcion',
    ),
]
