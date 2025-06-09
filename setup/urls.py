from django.contrib import admin
from django.urls import path
from galeria.views import buscar, index, imagem
from usuarios.views import login, cadastro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("imagem/<int:foto_id>", imagem, name="imagem"),
    path("buscar/", buscar, name="buscar"),
    path("login/", login, name="login"),
    path("cadastro/", cadastro, name="cadastro"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
