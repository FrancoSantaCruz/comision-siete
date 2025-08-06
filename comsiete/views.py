# Solicitud HTTP
# Solicitudes entrantes -> request
# Devolver respuestas -> response
from django.shortcuts import render
from apps.noticias.models import Noticia

# Devolver la página principal de mi sitio.
def inicio(request):
    noticias = Noticia.objects.all()
    context = {
        "noticias": noticias
    }
    return render(request, 'index.html', context)
