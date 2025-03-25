from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Base de datos en memoria (simulación)
items = [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Telefono"}]

@csrf_exempt # Desactiva la verificación CSRF para pruebas
def obtener_agregar_items(request):
    if request.method == 'GET': # Devolver la lista de ítems en formato JSON
        return JsonResponse(items, safe=False)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body) # Convertir JSON en diccionario
            nuevo_item = { "id": len(items) + 1,
            "nombre": data.get("nombre", "Sin nombre")}
            items.append(nuevo_item) # Agregar el nuevo ítem a la lista
            return JsonResponse(nuevo_item, status=201) # Respuesta
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)
        
@csrf_exempt
def obtener_un_item(request,id):
    if request.method == 'GET':
        posicion = next((i for i, dic in enumerate(items) if dic.get("id") == id), None)
        return JsonResponse(items[posicion], safe=False)

@csrf_exempt
def modificar_un_item(request,id,nombre):
    if request.method == 'GET':
        posicion = next((i for i, dic in enumerate(items) if dic.get("id") == id), None)
        items[posicion]["nombre"] = nombre
        return JsonResponse(items, safe=False)

@csrf_exempt
def eliminar_un_item(request,id):
    if request.method == 'GET':
        posicion = next((i for i, dic in enumerate(items) if dic.get("id") == id), None)
        items.pop(posicion)
        return JsonResponse(items, safe=False)