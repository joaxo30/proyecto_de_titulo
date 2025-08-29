from django.shortcuts import render, redirect
from .models import Registro

def Compra(request):
    return render(request, 'catalogo.html')


def resgistrarCliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre'),
        apellido = request.POST.get('apellido'),
        edad = request.POST.get('edad'),
        fecha = request.POST.get('fecha'),
        descripcion = request.POST.get('descripcion'),
        imagen = request.FILES.get('imagen'),
    
        registro = Registro(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            fecha_nacimiento=fecha,
            descripcion=descripcion,
            imagen=imagen
        )
        registro.save()
        return redirect('Compra')
    
    return render(request, 'registro.html')