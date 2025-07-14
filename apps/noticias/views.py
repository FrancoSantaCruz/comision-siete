from django.shortcuts import render
from .models import Noticia, Autor, Categoria

# Read
def todas_las_noticias(request):
    
    noticias = Noticia.objects.all() # SELECT * FROM Noticia;

    for noticia in noticias:
        print("*********")
        print(noticia.titulo)
        print(noticia.subtitulo)
        print(noticia.autor.nombre)
        print("*********")

    return render(request, 'todas_noticias.html')




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