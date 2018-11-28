from django.urls import path, include
from .views import agregar_mascota,listar_mascotas,eliminar_mascota,modificar_mascota

urlpatterns = [
   path('listar-mascotas/', listar_mascotas, name="api_listar_mascotas"),
   path('agregar-mascota/', agregar_mascota, name="api_agregar_mascota"),
   path('eliminar-mascota/<id>/', eliminar_mascota, name="api_eliminar_mascota"),
   path('modificar-mascota/', modificar_mascota, name="api_modificar_mascota"),
]