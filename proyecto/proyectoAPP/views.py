from django.shortcuts import render

def Compra(request):
    return render(request, 'catalogo.html')


def resgistrarCliente(request):
    return render(request, 'registro.html')