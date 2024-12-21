from django.urls import path 
from . import vistas  


urlpatterns = [
    path('', vistas.pagina_inicio, name='pagina_inicio'),
    path('inscritos/', vistas.lista_inscritos, name='lista_inscritos'),
    path('inscritos/crear/', vistas.crear_inscrito, name='crear_inscrito'),
    path('inscritos/editar/<int:pk>/', vistas.editar_inscrito, name='editar_inscrito'),
    path('inscritos/eliminar/<int:pk>/', vistas.eliminar_inscrito, name='eliminar_inscrito'),
    path('instituciones/', vistas.lista_instituciones, name='lista_instituciones'),
    path('instituciones/crear/', vistas.crear_institucion, name='crear_institucion'),
    path('instituciones/editar/<int:pk>/', vistas.editar_institucion, name='editar_institucion'),
    path('instituciones/eliminar/<int:pk>/', vistas.eliminar_institucion, name='eliminar_institucion'),
    path('api/autor/', vistas.autor_api, name='api_autor'),
    path('api/vista-inscritos/', vistas.api_vista_inscritos, name='api_vista_inscritos'),
    path('api/vista-instituciones/', vistas.api_vista_instituciones, name='api_vista_instituciones'),
    path('api/inscritos/', vistas.InscritoAPIListadoCrear.as_view(), name='api_lista_inscritos'),
    path('api/inscritos/<int:pk>/', vistas.InscritoAPIDetalle.as_view(), name='api_detalle_inscrito'),
    path('api/instituciones/', vistas.lista_instituciones_api, name='api_lista_instituciones'),
    path('api/instituciones/<int:pk>/', vistas.detalle_institucion_api, name='api_detalle_institucion'),
    path('api/vista-autor/', vistas.api_vista_autor, name='api_vista_autor'),
]
