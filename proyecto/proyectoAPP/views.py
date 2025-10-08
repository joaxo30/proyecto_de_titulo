from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Registro

def inicio(request):
    return render(request, 'inicio.html', {
        'usuario_nombre': request.session.get('usuario_nombre')
    })

def login_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        password = request.POST.get('password')

        try:
            usuario = Registro.objects.get(nombre=nombre)
            if check_password(password, usuario.password):
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                return redirect('inicio')
            else:
                messages.error(request, "Contraseña incorrecta")
        except Registro.DoesNotExist:
            messages.error(request, "El usuario no existe")

    return render(request, 'login.html')


def salir(request):
    request.session.flush()
    messages.success(request, "Sesión cerrada correctamente")
    return redirect('login')

def registrarCliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        password = request.POST.get('password')  
        fecha = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')

        password_encriptada = make_password(password)

        registro = Registro(
            nombre=nombre,
            apellido=apellido,
            password=password_encriptada,  
            fecha_nacimiento=fecha,
            descripcion=descripcion,
            imagen=imagen
        )
        registro.save()
        return redirect('login')
    
    return render(request, 'registro.html')

def gproductos(request):
    return render(request, 'gproductos.html')