"""citixen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from api.api import UserAPI
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', views.ProductoViewSet)
router.register('categoria', views.CategoriaViewSet)
#router.register('comprar_producto',views.MarcarProductoViewSet)
router.register('lista_productos_cliente', views.ListarProductosCompradosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/registrar_usuario/', include('rest_auth.registration.urls')),
    path('api/v1/auth/opciones_usuario/', include('rest_auth.urls')),
    path('api/v1/crear/', include(router.urls)),
    path('api/v1/comprados/', views.MarcarProducto.as_view()),
    path('api/1.0/create_user/', UserAPI.as_view(), name='api_create_user'),

]
