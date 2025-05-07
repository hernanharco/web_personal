from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # readonly_fields es una tupla que contiene los campos que serán de solo lectura en el panel de administración

admin.site.register(Project, ProjectAdmin)
# El modelo Project se registra en el panel de administración utilizando el ProjectAdmin como configuración personalizada