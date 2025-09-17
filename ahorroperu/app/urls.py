from django.urls import path
from app.view import producto, objeto, persona

####
urlpatterns =[
    path('', persona.listar_persona, name='listar_persona'),
    path('personas/', persona.listar_persona, name='listar_persona'),
    path('persona/nuevo/', persona.crear_persona, name='crear_persona'),
    path('persona/<int:id>/editar', persona.actualizar_persona, name='actualizar_persona'),
    path('persona/<int:id>/eliminar', persona.eliminar_persona, name='eliminar_persona'),

    path('', objeto.listar_objeto, name='listar_objeto'),
    path('objetos/', objeto.listar_objeto, name='listar_objeto'),
    path('objeto/nuevo/', objeto.crear_objeto, name='crear_objeto'),
    path('objeto/<int:id>/editar', objeto.actualizar_objeto, name='actualizar_objeto'),
    path('objeto/<int:id>/eliminar', objeto.eliminar_objeto, name='eliminar_objeto'),

    path('', producto.listar_producto, name='listar_producto'),
    path('productos/', producto.listar_producto, name='listar_producto'),
    path('producto/nuevo/', producto.crear_producto, name='crear_producto'),
    path('producto/<int:id>/editar', producto.actualizar_producto, name='actualizar_producto'),
    path('producto/<int:id>/eliminar', producto.eliminar_producto, name='eliminar_producto'),
]