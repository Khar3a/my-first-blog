"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
#Esta línea dice que para cada URL que empieza con admin/ Django encontrará su correspondiente view.
#amos, añade la línea para importar blog.urls.
#Tú también necesitarás cambiar la línea desde django.urls... porque estaremos usando la función include aquí, así que se necesitará añadir ese import a la línea.
#Ahora Django redirigirá todo lo que entre a 'http://127.0.0.1:8000/' hacia blog.urls y buscará más instrucciones allí.