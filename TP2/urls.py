from django.urls import path
from .api import AnuncioDetalleAPIView, CategoriaDetalleAPIView, CategoriaListaAPIView, AnuncioListaAPIView

app_name = 'anuncio'
urlpatterns = [
    path('api-view/categoria/', CategoriaListaAPIView.as_view()),
    path('api-view/categoria/<pk>/', CategoriaDetalleAPIView.as_view()),
    path('api-view/anuncio/', AnuncioListaAPIView.as_view()),
    path('api-view/anuncio/<pk>/', AnuncioDetalleAPIView.as_view()),
]