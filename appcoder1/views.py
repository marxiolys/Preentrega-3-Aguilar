from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, "appcoder1/inicio.html")

def estudiantes(request):
    return render(request, "appcoder1/estudiantes.html")

def profesores(request):
    return render(request, "appcoder1/profesores.html")

def cursos(request):
    return render(request, "appcoder1/cursos.html")
