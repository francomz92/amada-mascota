from django.urls import path
from index.views import Index

app_name = 'index'

urlpatterns = [
    path(
        '',
        Index.as_view(),
        name='index',
    ),
]
