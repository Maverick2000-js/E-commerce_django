# from django.shortcuts import render

# # Create your views here.

# from django.http import HttpResponse

# def catalogo(request):
#     return HttpResponse("Catálogo de libros disponible")

# libros/views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import queries

def catalogo(request):
    libros = queries.obtener_libros_disponibles()
    return JsonResponse(libros, safe=False)

def detalle(request, libro_id):
    libro = queries.obtener_libro_por_id(libro_id)
    if libro is None:
        return JsonResponse({"error": "Libro no encontrado"}, status=404)
    return JsonResponse(libro)

@csrf_exempt
def crear(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)
    datos = json.loads(request.body)
    nuevo_id = queries.crear_libro(
    titulo=datos["titulo"],
    precio=datos["precio"],
    publicado_en=datos["publicado_en"],
    autor_id=datos["autor_id"],
    )
    return JsonResponse({"id": nuevo_id}, status=201)

@csrf_exempt
def actualizar(request, libro_id):
    if request.method != "PUT":
        return JsonResponse({"error": "Método no permitido"}, status=405)
    datos = json.loads(request.body)
    queries.actualizar_precio(libro_id, datos["precio"])
    return JsonResponse({"mensaje": "Libro actualizado"}, status=200)

@csrf_exempt
def eliminar(request, libro_id):
    if request.method != "DELETE":
        return JsonResponse({"error": "Método no permitido"}, status=405)
    queries.eliminar_libro(libro_id)
    return JsonResponse({"mensaje": "Libro eliminado"}, status=204)

