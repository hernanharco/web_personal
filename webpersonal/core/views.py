
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html') # Renderiza la plantilla 'home.html' ubicada en la carpeta 'core/templates/core/'
# La función render toma el objeto de solicitud y la ruta de la plantilla como argumentos y devuelve una respuesta HTTP con el contenido de la plantilla renderizada
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')

