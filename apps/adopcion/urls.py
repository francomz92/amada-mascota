from django.urls import path
from apps.adopcion.views import PrivateAdopcion, PrivateCreateAdopcion, PrivateUpdateAdopcion, PublicAdopcion, PublicDetailAdopcion

app_name = 'adopcion'

urlpatterns = [
    path(
        'adopcion/',
        PublicAdopcion.as_view(),
        name='public_adopcion',
    ),
    path(
        'adopcion/mis-publicaciones/',
        PrivateAdopcion.as_view(),
        name='private_adopcion',
    ),
    path(
        'adopcion/publicar/',
        PrivateCreateAdopcion.as_view(),
        name='private_create_adopcion',
    ),
    path(
        'adopcion/editar/<int:id>/',
        PrivateUpdateAdopcion.as_view(),
        name='private_update_adopcion',
    ),
    path(
        'adopcion/<int:id>/',
        PublicDetailAdopcion.as_view(),
        name='public_detail_adopcion',
    ),
]