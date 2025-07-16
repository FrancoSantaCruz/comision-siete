from django.urls import path
# from .views import todas_las_noticias, una_noticia, noticia_categoria, crear_noticia, actualizar_noticia, eliminar_noticia

from .views import TodasLasNoticiasView, UnaNoticiaView, CrearNoticiaView, ActualizarNoticiaView, EliminarNoticiaView

#http://127.0.0.1:8000/noticias/

urlpatterns = [
    # path('', todas_las_noticias, name='todas_las_noticias'),
    # path('detalle/', una_noticia, name='una_noticia'),
    # path('categoria/', noticia_categoria, name='noticia_categoria'),
    # path('crear/', crear_noticia, name='crear_noticia'),
    # path('actualizar/', actualizar_noticia, name='actualizar_noticia'),
    # path('eliminar/', eliminar_noticia, name='eliminar_noticia')

    path('', TodasLasNoticiasView.as_view(), name="todas_las_noticias"),
    path('<int:noticia_id>/', UnaNoticiaView.as_view(), name='una_noticia'),
    path('crear/', CrearNoticiaView.as_view(), name='crear_noticia'),
    path('actualizar/<int:noticia_id>/', ActualizarNoticiaView.as_view(), name='actualizar_noticia'),
    path('eliminar/<int:noticia_id>/', EliminarNoticiaView.as_view(), name='eliminar_noticia')
]