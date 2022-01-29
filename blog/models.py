#Creas tu modelo, aqui se definen todos los llamdos Models
#Aqui se define nuestra entrada del blog
#Todas las líneas que comienzan con from o import son líneas para agregar algo de otros archivos.
from django.conf import settings
from django.db import models
from django.utils import timezone


#class Post(models.Model):, esta línea define nuestro modelo (es un objeto).
#class es una palabra clave que indica que estamos definiendo un objeto.
#Post es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Siempre inicia el nombre de una clase con una letra mayúscula.
#models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Se definen las propiedades como title, text, creted_date, published_date, author
#models.CharField, así es como defines un texto con un número limitado de caracteres.
#models.TextField, este es para texto largo sin límite. 
#models.DateTimeField, este es fecha y hora.
#modelos.ForeignKey, este es una relación (link) con otro modelo.

#def publish(self):, Es exactamente el método publish que mencionábamos antes. def significa
#que es una función/método y publish es el nombre del método. Puedes cambiar el nombre del método

#Los métodos suelen devolver (return, en inglés) algo. Hay un ejemplo de esto en el método __str__. En este escenario, cuando llamemos a __str__() obtendremos un texto (string) con un título de Post.
#nota que ambos def publish(self):, y def __str__(self): son indentados dentro de nuestra clase. Porque Python es sensible a los espacios en blancos, necesitamos indentar nuestros métodos dentro de la clase. 
#De lo contrario, los métodos no pertenecen a la clase, y puedes obtener un comportamiento inesperado.