from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Producto 



# Create your views here.

from django.http import HttpResponse


def lista_productos(request):
    return render (request, 'lista_productos.html')

def crea_productos(request):
    return render (request, 'crear.html')

def eliminar_producto(request, producto_id):
    # Buscamos el producto por su ID (Primary Key)
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == 'POST':
        producto.delete() 
        return JsonResponse({'status': 'ok', 'message': 'Producto eliminado correctamente'}, status=200) # Redirecciona a tu vista principal
        
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def listar_productos(request):
    productos= Producto.objects.all()
    data = []

    for p in productos:
        data.append({
        'id': p.id,
        'nombre': p.nombre,
        'precio': str(p.precio),
        'descripcion': p.descripcion or '',
        'imagen': p.imagen.url if p.imagen else ''
        })

    return JsonResponse(data, safe=False)

@csrf_exempt
def crear_producto(request):
    if request.method == 'POST':
        producto = Producto.objects.create(
            nombre=request.POST.get('nombre', '').strip(),
            precio=request.POST.get('precio'),
            descripcion=request.POST.get('descripcion', '').strip(),
            imagen=request.FILES.get('imagen')
        )

        return JsonResponse({
            'mensaje': 'Producto creado exitosamente',
            'descripcion': producto.descripcion
        }, status=201)

    return JsonResponse(
        {'error': 'Método no permitido'},
        status=405
    )