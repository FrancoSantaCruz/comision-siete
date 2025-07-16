from django.shortcuts import render
from .models import Noticia, Autor, Categoria

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

'''
    VISTAS BASADAS EN CLASES (CBV)
'''
class TodasLasNoticiasView(ListView):
    model = Noticia
    template_name = 'todas_noticias.html'
    context_object_name = 'noticias'


class UnaNoticiaView(DetailView):
    model = Noticia
    template_name = 'una_noticia.html'
    context_object_name = 'noticia'
    pk_url_kwarg = 'noticia_id'


class CrearNoticiaView(CreateView):
    model = Noticia
    template_name = 'nueva_noticia.html'
    fields = ['titulo', 'subtitulo', 'contenido']
    success_url = reverse_lazy('todas_las_noticias')


class ActualizarNoticiaView(UpdateView):
    model = Noticia
    template_name = 'actualizar_noticia.html'
    fields = ['titulo', 'subtitulo']
    success_url = reverse_lazy('todas_las_noticias')
    pk_url_kwarg = 'noticia_id'


class EliminarNoticiaView(DeleteView):
    model = Noticia
    template_name = 'eliminar_noticia.html'
    success_url = reverse_lazy('todas_las_noticias')
    pk_url_kwarg = 'noticia_id'

'''
    VISTAS BASADAS EN FUNCIONES (FBV)
'''

def todas_las_noticias(request):
    # BUSQUEDA DE INFORMACION GUARDADA
    noticias = Noticia.objects.all()


    #LOGICA REQUERIDA


    # CONSTRUCCION DE LA RESPUESTA
    context = {
        'noti': noticias
    }

    return render(request, 'todas_noticias.html', context)

def una_noticia(request): 

    noticia = Noticia.objects.get(noticia_id=3)

    print(noticia.titulo)
    print(noticia.subtitulo)
    print(noticia.contenido)

    return render(request, 'una_noticia.html')

def noticia_categoria(request):

    noticias_politica = Noticia.objects.filter(categorias__nombre="Politica")
    print("Noticias en categoría 'Política':")
    for noticia in noticias_politica:
        print(f"    {noticia.titulo} - escrito por: {noticia.autor.nombre}")

    return render(request, 'politica_noticias.html')

# Create
def crear_noticia(request):

    cat = Categoria.objects.get(categoria_id=3)
    autor = Autor.objects.get(autor_id=2)

    nueva_noticia = Noticia(
        titulo="Noticia en clase 1", 
        subtitulo="Subtitulo en clase 1", 
        contenido="Contenido en clase 1",
        autor=autor
        )
    
    nueva_noticia.save()
    nueva_noticia.categorias.set([cat])

    print("------------")
    print(nueva_noticia.titulo)
    print(nueva_noticia.subtitulo)
    print(nueva_noticia.contenido)
    print(nueva_noticia.autor.nombre)
    print("------------")

    return render(request, 'nueva_noticia.html')

# Update
def actualizar_noticia(request):

    noticia_actual = Noticia.objects.filter(titulo="Noticia en clase 2 MODIFICADO").first()

    noticia_actual.titulo = "Noticia en clase 3 MODIFICADOx2"
    noticia_actual.subtitulo = "Subtitulo en clase 3 MODIFICADOx2"

    noticia_actual.save()

    print("------------")
    print(noticia_actual.titulo)
    print(noticia_actual.subtitulo)
    print(noticia_actual.contenido)
    print(noticia_actual.autor.nombre)
    print("------------")

    return render(request, 'actualizar_noticia.html')

# Delete
def eliminar_noticia(request):
    noticia = Noticia.objects.get(noticia_id=14)
    noticia.delete()

    print("NOTICIA ELIMINADA CON EXITO")

    return render(request, 'eliminar_noticia.html')



