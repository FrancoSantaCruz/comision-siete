from django.urls import path
from .views import (
    TodasLasNoticiasView, 
    UnaNoticiaView, 
    CrearNoticiaView, 
    ActualizarNoticiaView, 
    EliminarNoticiaView,
    todas_las_noticias,
    # una_noticia,
    # eliminar_noticia
)

app_name = "apps.noticias"

urlpatterns = [
    # CBV http://127.0.0.1:8000/noticias/cbv/
    # path('', TodasLasNoticiasView.as_view(), name="todas_las_noticias"),
    path('<int:noticia_id>/', UnaNoticiaView.as_view(), name='una_noticia'),
    path('crear/', CrearNoticiaView.as_view(), name='crear_noticia'),
    path('actualizar/<int:noticia_id>/', ActualizarNoticiaView.as_view(), name='actualizar_noticia'),
    path('eliminar/<int:noticia_id>/', EliminarNoticiaView.as_view(), name='eliminar_noticia'),

    # FBV http://127.0.0.1:8000/noticias/fbv/
    path('', todas_las_noticias, name="todas_las_noticias"),
    # path('fbv/<int:noticia_id>/', una_noticia, name="una_noticia_fbv"),
    # path('fbv/eliminar/<int:noticia_id>/', eliminar_noticia, name="eliminar_noticia_fbv"),
]