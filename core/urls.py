


from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, clientes, contratos, cupones, historial, planes, usuarios, nuevo_cliente, modificar_cliente, eliminar_cliente, nuevo_planes, modificar_planes, eliminar_planes, nuevo_contrato, modificar_contrato, eliminar_contrato

urlpatterns = [
    path('', home, name="home"),
    path('clientes/', clientes, name="clientes"),
    path('contratos/', contratos, name="contratos"),
    path('cupones/', cupones, name="cupones"),
    path('historial/', historial, name="historial"),
    path('planes/', planes, name="planes"),
    path('usuarios/', usuarios, name="usuarios"),
    path('nuevo_cliente/', nuevo_cliente, name="nuevo_cliente"),
    path('modificar_cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar_cliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
    path('nuevo_planes/', nuevo_planes, name="nuevo_planes"),
    path('modificar_planes/<id>/', modificar_planes, name="modificar_planes"),
    path('eliminar_planes/<id>/', eliminar_planes, name="eliminar_planes"),
    path('nuevo_contrato/', nuevo_contrato, name="nuevo_contrato"),
    path('modificar_contrato/<id>/', modificar_contrato, name="modificar_contrato"),
    path('eliminar_contrato/<id>/', eliminar_contrato, name="eliminar_contrato"),
]