from .paths.profile import profile_urls
from .paths.reset import reset_urls
from .paths.auth import auth_urls

app_name = 'usuario'

urlpatterns = auth_urls + reset_urls + profile_urls