from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all() # Obtiene todos los objetos del modelo Project
    return render(request, 'portfolio/portfolio.html', {'projects': projects}) # Renderiza la plantilla 'portfolio.html' y pasa los proyectos como contexto  
# La función render toma el objeto de solicitud y la ruta de la plantilla como argumentos y devuelve una respuesta HTTP con el contenido de la plantilla renderizada
