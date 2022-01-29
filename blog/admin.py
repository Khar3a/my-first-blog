#Para agregar, editar y borrar los posts que hemos modelado, usaremos el administrador (admin) de Django.
# Register your models here.

from django.contrib import admin
from .models import Post

admin.site.register(Post)

 #importamos (incluimos) el modelo Post definido en el capítulo anterior. Para hacer nuestro modelo 
 #visible en la página del administrador, tenemos que registrar el modelo con admin.site.register(Post).
