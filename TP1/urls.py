from django.urls import path
from .views import obtener_agregar_items, obtener_un_item, modificar_eliminar_item

urlpatterns = [
path('items/', obtener_agregar_items, name='obtener_agregar_items'),
path('items/<int:id>', obtener_un_item, name='obtener_un_item'),
path('items/modificar/<int:id>', modificar_eliminar_item, name='modificar_eliminar_item'),
]
