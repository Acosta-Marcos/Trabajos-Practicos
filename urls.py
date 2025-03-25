from django.urls import path
from .views import obtener_agregar_items, obtener_un_item, modificar_un_item, eliminar_un_item

urlpatterns = [
path('items/', obtener_agregar_items, name='obtener_agregar_items'),
path('items/<int:id>', obtener_un_item, name='obtener_un_item'),
path('items/modificar/<int:id>/<str:nombre>/', modificar_un_item, name='modificar_un_item'),
path('items/eliminar/<int:id>', eliminar_un_item, name='eliminar_un_item'),
]
