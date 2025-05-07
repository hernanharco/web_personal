# web_personal
django

1. Crear el entorno virtual
 - pip install virtualenv
 - python -m venv venv
 - .\venv\Scripts\activate
 - pip install django
 - django-admin startproject django_crud_api .
 - python manage.py runserver
 - python manage.py migrate 
___________________________________

2. Vamos a crear una vista para esto vamos a 
 - python manage.py startapp core -> de esta forma crea toda la información con la que debemos trabajar
 - views.py
 - ahora vamos a la clase url.py y unimos con la funcion que se crea en views.py
_________________________________________

3. Vamos a crear los templates en donde vamos a crear los html
 - Creamos templates a nivel de core
  - core
   - home.html
   - ahora en en views modificamos la funciones para que estas comience a llamar los templates
	- def home(request)
		return render(request, "core/home.html"
 3.1 A pesar que estamos haciendo todo el proceso va a sacar un error esto pasa porque falta core
	- Vamos a settings.py en webpersonal
	 - En la parte de INSTALLED_APPS = [ colocamos 'core', ] -> despues de la informacion que hay ahi
___________________________________

4. Para que el codigo no sea redudante
 - en templates > core > creamos base.html
  - en la parte de base.html ingresamos {block content %}    {% endblock %} que esto sirve para comenzar a unir nuestras paginas
  - igual en cada html creado en core debemos agregar
	{% extends 'core/base.html' %}´

	{block content %}

	<h2>Contacto</h2>
	<p>Me puedes contactar aqui</p>

	{% endblock %}
___________________________________

5. Hacer el tempalte tag url de forma dinamica -> buenas practicas
 - vamos hacer los enlaces relativos
  - base.html
	dentro del href="{% url 'home' %}"
___________________________________

6. Uniendo el Frontend con el Backend
 Esta parte lo que hacemos en modificar base.html con un html que el profesor ya tenia en guardado y se comienzan hacer la modificaciones
 para que funcione con los tag correspondientes y tambien creamos la carpeta static a nivel core para agregar archivos ya creados
 
 6.1 Haciendo que la cabecera sea dinamica
  - {% block title %} Home {% endblock %}

	{% comment %} para que pueda aparecer la imagen de fondo se debe dejar todo el codigo en una sola linea {% endcomment %}
	{% block background %}{% load static %}{% static 'core/img/home-bg.jpg' %}{% endblock %}

	{% block headers %}

	  <h1>Hernan A. Cortés</h1>
	  <span class="subheading">Programador Full Stack</span>

	{% endblock %}

7. En este punto se comienza a maquetar la pagina de internet con su respectivos tag
___________________________________

8. Gestionando Portfolio
 - hay que esta ubicado en la terminal en webpersonal en donde esta ubicado el setting
 - Hay una forma de activa el entorno virtual de forma rapida es.
  - se va manage.py presiona boton derecho y run python file in terminal
  8.1 pip install Pillow -> paquete para la manipulacion de imagenes
   8.1.1 Definiendo el Mapeo / Estructura de los proyectos
    - Creamos un Projecto nuevo para crear ahi los modelos que es donde creamos la base de datos
	 python manage.py startapp portfolio
	  - y trabajamos en la clase models.py
   8.1.2 Vamos a settings.py y en la parte de INSTALLED_APPS = [ 'portfolio' ]
    vamos a migrar la base de datos 
	 - python manage.py makemigrations portfolio
   8.1.3 Debemos migrar esta informacion a la base de datos
    - python manage.py migrate portfolio
___________________________________

9. El panel de Administrador
 - Colocamos el programa a correr e ingresamos a 
  /admin -> va a pedir el usuario y contraseña
   1. python manage.py createsuperuser
    Username: xxxxxx
	email address: xxxxxx
	password: xxxxxx
	password (again): xxxxxx
   2. Vamos a admin.py -> esto es para registrarlo para que se pueda ver en /admin
   
   9.1 Personalizando el Administrador
    - Si queremos que aparezca un nombre adecuado le agregamos en 
	portfolio > apps.py colocamos verbose_name = 'Portafolio'
	- despues vamos a settings.py y vamos agregar este cambio en para que haga la configuracion extendida 
	 INSTALLED_APPS = [ 'portfolio.apps.PortfolioConfig' ]
   
   9.2 Cambiando el nobmre del Modelo
    - en models.py vamos agregar la class Meta: 
	- verbose_nama -> lo que hacemos en cambiar el nombre al que queremos mostrar 

   9.3 Created y Updated no se muestra en pantalla de /admin hacemos lo siguiente para que se pueda mostrar
    - en admin.py vamos a crear una class Project para extender 
	
   9.4 Creamos un directorio media para guardar las imagenes  para esto creamos un carpeta a nivel raiz
    - webpersonal y creamos media
	- vamos a settings.py y colocamos los ficheros staticos a mano #Media Files
	- vamos al models.py ubicado en portfolio y agregamos un campo extra en image 
	
   9.5 Si presionamos en el entorno de admin este no muestra la imagen y para que la muestre vamos hacer lo siguiente
    - en urls.py en webpersonal en la parte donde se encuentra el settings.py
	 - colocamos el from django.conf import settings para que cargue el fichero settings y cargue las dos variables de media
	 y colocamos el if setting.DEBUG: -> Que mira si estamos en modo debug entonces ejecutara la imagenes
___________________________________

10. El Patron MVT: Modelo - Vista - Template
 10.1 Vamos a views.py y colocamos el url del portfolio en este lugar
 10.2 creamos template > portfolio y colocamos el archivo portfolio.html que estaba ubicado en core
 10.3 vamos a views.py de portfolio e ingresamos algunos lineas de codigo e instalamos
  - pip install pylint-django
  lo que se hace en views es poder tener acceso a la base de datos y poder trabajar con la informacion guardada
 10.4 Vamos a portfolio.html y hacemos la modificaciones pertinentes para que comience a llamar la información y se muestre en frontend y asi queda un contenido dinamico
___________________________________

11. Para finalizar vamos agregar un nuevo campo a la base de datos que es link
 11.1 Como se hizo una modificacion debemos volver hacer este cambio se hace models.py
  - python manage.py makemigrations portfolio
  - python manage.py migrate portfolio
 11.2 Ahora vamos portfolio.html