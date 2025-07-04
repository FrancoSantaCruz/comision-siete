from django.shortcuts import render

def todas_las_noticias(request):
    return render(request, 'todas_noticias.html')

def una_noticia(request): 
    return render(request, 'una_noticia.html')

def noticia_categoria_politica(request):
    return render(request, 'politica_noticias.html')