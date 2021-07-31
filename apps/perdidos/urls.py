from django.urls import path
from apps.perdidos.views import PrivateCreatePerdidos, PrivatePerdidos, PrivateUpdatePerdidos, PublicDetailPerodidos, PublicPerdidos

app_name = 'perdidos'

urlpatterns = [
    path(
        'perdidos/',
        PublicPerdidos.as_view(),
        name='public_perdidos',
    ),
    path(
        'perdidos/mis-publicaciones/',
        PrivatePerdidos.as_view(),
        name='private_perdidos',
    ),
    path(
        'perdidos/publicar/',
        PrivateCreatePerdidos.as_view(),
        name='private_create_perdidos',
    ),
    path(
        'perdidos/editar/<int:id>/',
        PrivateUpdatePerdidos.as_view(),
        name='private_update_perdidos',
    ),
    path(
        'perdidos/<int:id>/',
        PublicDetailPerodidos.as_view(),
        name='public_detail_perdidos',
    ),
]