#Una View es un lugar donde ponemos la "lógica" de nuestra aplicación. Pedirá información del modelo que has creado antes y se la pasará a la plantilla.

from django.shortcuts import render

# Create your views here.
#Se creo una función (def) llamada post_list que acepta request y return una función render que reproduce (construye) nuestra plantilla blog/post_list.html

def post_list(request):
    return render(request, 'blog/post_list.html', {})
