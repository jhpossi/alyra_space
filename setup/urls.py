from django.contrib import admin
from django.urls import path
from galeria.views import buscar, index, imagem
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("imagem/<int:foto_id>", imagem, name="imagem"),
    path("buscar/", buscar, name="buscar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
