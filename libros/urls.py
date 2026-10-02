# # libros/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [path('', views.catalogo, name= 'inicio')]

# libros/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('<int:libro_id>/', views.detalle, name='detalle'),
    path('crear/', views.crear, name='crear'),
    path('<int:libro_id>/actualizar/', views.actualizar, name='actualizar'),
    path('<int:libro_id>/eliminar/', views.eliminar, name='eliminar'),
]
