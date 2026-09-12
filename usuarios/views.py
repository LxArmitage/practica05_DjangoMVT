from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# ============================================================
# VISTA: INICIO
# ============================================================
def inicio(request):
    rol = None

    # Verificar si existe un usuario autenticado
    if request.user.is_authenticated:
        try:
            rol = request.user.perfilusuario.rol.nombre
        except:
            rol = "Sin rol asignado"

    contexto = {
        "titulo": "Control de Usuarios",
        "mensaje": "Bienvenido a la Práctica 05 con Django",
        "rol": rol
    }
    return render(
        request,
        "usuarios/inicio.html",
        contexto
    )


# ============================================================
# VISTA: INICIAR SESIÓN
# ============================================================
def iniciar_sesion(request):
    # Si el usuario presiona el botón Ingresar
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verificar usuario y contraseña
        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        # Si las credenciales son correctas
        if usuario is not None:
            login(request, usuario)
            return redirect("inicio")

        # Si las credenciales son incorrectas
        contexto = {
            "error": "Usuario o contraseña incorrectos"
        }
        return render(
            request,
            "usuarios/login.html",
            contexto
        )

    # Primera vez que se solicita /login/
    return render(
        request,
        "usuarios/login.html"
    )
