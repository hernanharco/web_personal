from django.db import models

# Create your models here.
# En esta parte es la creacion de la base de datos
class Project(models.Model):
    title = models.CharField(max_length=100,verbose_name='Título')
    # El campo title es un CharField con un máximo de 100 caracteres y un nombre legible para el administrador
    description = models.TextField(verbose_name='Descripción')
    # El campo description es un TextField y tiene un nombre legible para el administrador
    image = models.ImageField(verbose_name='Imagen', upload_to='projects/')
    # El campo image es un ImageField que permite subir imágenes y se guardará en la carpeta 'projects/'
    link = models.URLField(verbose_name='Direccion Web', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') 
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    # El campo created es un DateTimeField que se establece automáticamente al crear el objeto y tiene un nombre legible para el administrador
     
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created'] # Ordenar por fecha de creación (más reciente primero)

    def __str__(self):
        return self.title # Devuelve el título del proyecto como representación en cadena del objeto
