from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.models import User

def lista_clientes(request):
    clientes = User.objects.all().order_by('username')
    return render(request,'clientes/lista_clientes.html',{'clientes': clientes })


def crear_cliente(request):
    if request.method == 'POST':
        # captura los datos del formulario para crear un usuario y guardarlo
        username = request.POST.get('username', "" ).strip()       
        first_name = request.POST.get('first_name', "" ).strip()       
        last_name = request.POST.get('last_name', "" ).strip()       
        email = request.POST.get('email', "" ).strip()       
        password = request.POST.get('password', "" ).strip() 

        errores = { } 

        if not username:
            errores["username"] = "El usuario es obligatorio"
        elif User.objects.filter(username = username).exists():
            errores["username"] = "El usuario ya existe"
        if not email:
            errores["email"] = "El email es obligatorio"
        if not password or len(password) < 8:
            errores["password"]= "El password es obligatorio y debe tener más de 8 caracteres"
        if errores:
            return render(request, 'clientes/crear_cliente.html', {
                'errores': errores,
                'datos': request.POST
            })

        User.objects.create_user(
            username= username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password
        )

        return redirect('clientes:lista_clientes' )
    return render(request, 'clientes/crear_cliente.html')



