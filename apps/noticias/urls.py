from django.urls import path
from .views import todas_las_noticias, una_noticia, noticia_categoria_politica

#http://127.0.0.1:8000/noticias/una/
urlpatterns = [
    path('todas/', todas_las_noticias, name='todas_las_noticias'), # http://127.0.0.1:8000/noticias/todas/
    path('una/', una_noticia, name='una_noticia'), # http://127.0.0.1:8000/noticias/una/
    path('politica/', noticia_categoria_politica, name='noticia_categoria_politica'), # http://127.0.0.1:8000/noticias/politica/
]