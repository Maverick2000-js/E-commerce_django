from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('crear/', views.crea_productos, name='crea_productos'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('api/productos/', views.listar_productos, name='listar_productos'),
    path('api/productos/crear/', views.crear_producto, name='crear_producto'),
]