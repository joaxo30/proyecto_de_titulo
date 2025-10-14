<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Producto

def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        rol = request.POST.get('rol')

        # Validar que el usuario no exista
        if Usuario.objects.filter(usuario=usuario).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('registro')

        # Crear usuario y encriptar contraseña
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            usuario=usuario,
            rol=rol
        )
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()

        messages.success(request, f'Usuario "{usuario}" registrado correctamente.')
        return redirect('registro')

    return render(request, 'registro.html')

# Login
def login_usuario(request):
    if request.method == 'POST':
        usuario_input = request.POST.get('usuario')
        password_input = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(usuario=usuario_input)
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
            return redirect('login')

        # Verificar contraseña
        if usuario.check_password(password_input):
            # Guardar datos en la sesión
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nombre'] = usuario.nombre
            request.session['usuario_rol'] = usuario.rol

            messages.success(request, f'Bienvenido {usuario.nombre} 👋')
            return redirect('inicio')
        else:
            messages.error(request, 'Contraseña incorrecta.')
            return redirect('login')
=======
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
>>>>>>> a9705f429470718141189b95948f86ca60e41f56

    return render(request, 'login.html')


<<<<<<< HEAD
# Logout
def logout_usuario(request):
    # Eliminar todos los datos de sesión
    request.session.flush()
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')

def login_requerido(func):
    def wrapper(request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            messages.error(request, 'Debes iniciar sesión primero.')
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper

def admin_requerido(func):
    def wrapper(request, *args, **kwargs):
        if 'usuario_rol' not in request.session or request.session['usuario_rol'] != 'admin':
            messages.error(request, 'No tienes permisos para acceder a esta sección.')
            return redirect('inicio')
        return func(request, *args, **kwargs)
    return wrapper

@login_requerido
@admin_requerido
def gestion_productos(request):
    # AGREGAR PRODUCTO
    if request.method == 'POST' and request.POST.get('action') == 'add':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        if not nombre or not categoria or not precio or not stock:
            messages.error(request, 'Todos los campos son obligatorios.')
        else:
            Producto.objects.create(
                nombre=nombre,
                categoria=categoria,
                precio=precio,
                stock=stock
            )
            messages.success(request, f'Producto "{nombre}" agregado correctamente.')
        return redirect('gproductos')

    # EDITAR PRODUCTO
    if request.method == 'POST' and request.POST.get('action') == 'edit':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, id=producto_id)
        producto.nombre = request.POST.get('nombre')
        producto.categoria = request.POST.get('categoria')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.save()
        messages.success(request, f'Producto "{producto.nombre}" editado correctamente.')
        return redirect('gproductos')

    # ELIMINAR PRODUCTO
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, id=producto_id)
        producto.delete()
        messages.success(request, f'Producto "{producto.nombre}" eliminado correctamente.')
        return redirect('gproductos')

    # Mostrar productos
    productos = Producto.objects.all()
    return render(request, 'gproductos.html', {'productos': productos})

=======
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
>>>>>>> a9705f429470718141189b95948f86ca60e41f56
