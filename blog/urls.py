# importando la función de Django path y todos nuestras views desde la aplicación blog

from django.urls import path
from . import views

#Patron URL
#estamos asociando una vista (view) llamada post_list a la URL raíz. Este patrón de URL coincidirá con una
#cadena vacía y el solucionador de URL de Django ignorará el nombre de dominio (es decir, http://127.0.0.1:8000/) 
#que prefija la ruta de URL completa. Este patrón le dirá a Django que views.post_list es el lugar correcto al que 
#ir si alguien entra a tu sitio web con la dirección 'http://127.0.0.1:8000/'.
#La última parte name='post_list' es el nombre de la URL que se utilizará para identificar a la vista.
urlpatterns = [
    path('', views.post_list, name='post_list'),
]