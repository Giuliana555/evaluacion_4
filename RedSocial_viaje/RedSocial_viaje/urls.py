"""
URL configuration for RedSocial_viaje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from publicacion.views import registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Rutas de autenticación
    path('accounts/register/', registro, name='register'),  # Registro
    path('accounts/logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),  # Logout
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),  # Redirige a login
    path('usuario/', include('usuario.urls')),
    path('publicacion/', include('publicacion.urls')),
    path('destino/', include('destino.urls')),
    path('api/', include('api_viajes.urls')),
<<<<<<< HEAD
]


=======
]
>>>>>>> e431b4f308c4ade594ee16bd9b3b60f0b7ad5787
