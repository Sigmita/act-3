# app_Netflix/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

# Página de inicio
def inicio_netflix(request):
    return render(request, 'inicio.html')

# Vista para mostrar todos los usuarios
def ver_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/ver_usuarios.html', {'usuarios': usuarios})

# Vista para agregar un nuevo usuario
def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        tipo_membresia = request.POST['tipo_membresia']
        pais = request.POST['pais']
        Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            tipo_membresia=tipo_membresia,
            pais=pais
        )
        return redirect('ver_usuarios')
    return render(request, 'usuario/agregar_usuario.html')

# Vista para actualizar un usuario (mostrar formulario)
def actualizar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    return render(request, 'usuario/actualizar_usuario.html', {'usuario': usuario})

# Vista para realizar la actualización del usuario
def realizar_actualizacion_usuario(request, id_usuario):
    if request.method == 'POST':
        usuario = get_object_or_404(Usuario, pk=id_usuario)
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.email = request.POST['email']
        usuario.tipo_membresia = request.POST['tipo_membresia']
        usuario.pais = request.POST['pais']
        usuario.save()
        return redirect('ver_usuarios')
    return redirect('ver_usuarios') # Redirecciona si no es POST

# Vista para borrar un usuario
def borrar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('ver_usuarios')
    return render(request, 'usuario/borrar_usuario.html', {'usuario': usuario})