from django.urls import path 
from . import vistas  


urlpatterns = [
    path('inscritos/', vistas.lista_inscritos, name='lista_inscritos'),
    path('inscritos/nuevo/', vistas.crear_inscrito, name='crear_inscrito'),
    path('inscritos/<int:pk>/editar/', vistas.editar_inscrito, name='editar_inscrito'),
    path('inscritos/<int:pk>/eliminar/', vistas.eliminar_inscrito, name='eliminar_inscrito'),
    path('api/inscritos/', vistas.InscritoAPIListadoCrear.as_view(), name='api_lista_inscritos'),
    path('api/inscritos/<int:pk>/', vistas.InscritoAPIDetalle.as_view(), name='api_detalle_inscrito'),
    path('api/instituciones/', vistas.InstitucionAPIListadoCrear.as_view(), name='api_lista_instituciones'),
    path('api/instituciones/<int:pk>/', vistas.InstitucionAPIDetalle.as_view(), name='api_detalle_institucion'),
    path('', vistas.pagina_inicio, name='pagina_inicio'),
    path('api/vista_inscritos/', vistas.api_vista_inscritos, name='api_vista_inscritos'),
    path('api/vista_instituciones/', vistas.api_vista_instituciones, name='api_vista_instituciones'),
    path('instituciones/', vistas.lista_instituciones, name='lista_instituciones'),
    path('instituciones/nueva/', vistas.crear_institucion, name='crear_institucion'),
    path('instituciones/<int:pk>/editar/', vistas.editar_institucion, name='editar_institucion'),
    path('instituciones/<int:pk>/eliminar/', vistas.eliminar_institucion, name='eliminar_institucion'),
]