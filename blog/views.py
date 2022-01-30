#Una View es un lugar donde ponemos la "lógica" de nuestra aplicación. Pedirá información del modelo que has creado antes y se la pasará a la plantilla.
# incluir el modelo que definimos en el archivo models.py
#El punto antes de models indica el directorio actual o la aplicación actual. Ambos, views.py y models.py están en el mismo directorio. Esto significa
#que podemos utilizar . y el nombre del archivo (sin .py). Ahora importamos el nombre del modelo (Post).

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
#Se creo una función (def) llamada post_list que acepta request y return una función render que reproduce (construye) nuestra plantilla blog/post_list.html

def post_list(request):
#Lista de post publicados ordenados por published_date (fecha de publicación
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
