from django.contrib import admin
from django.urls import path, include

from app.view import producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

    path('productos/pdf/', producto.generar_lista_productos_pdf, name='generar_lista_productos_pdf'),
]
