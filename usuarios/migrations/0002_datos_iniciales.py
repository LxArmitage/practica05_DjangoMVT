from django.db import migrations
from django.contrib.auth.hashers import make_password


ROLES = [
    ("Administrador", "Administra usuarios y roles"),
    ("Especialista", "Personal especializado"),
    ("Vendedor", "Personal de ventas"),
    ("Analista", "Personal de análisis"),
    ("Dueño", "Propietario del negocio"),
    ("Cliente", "Cliente registrado"),
]

# Usuarios de prueba: (username, password, rol)
USUARIOS = [
    ("oswaldoanalista", "probando", "Analista"),
    ("oswaldoduenio", "probando", "Dueño"),
    ("oswaldovendedor", "probando", "Vendedor"),
    ("oswaldoespecialista", "probando", "Especialista"),
    ("oswaldocliente", "probando", "Cliente"),
]


def cargar_datos(apps, schema_editor):
    Rol = apps.get_model("usuarios", "Rol")
    PerfilUsuario = apps.get_model("usuarios", "PerfilUsuario")
    User = apps.get_model("auth", "User")

    # Crear catálogo de roles
    roles = {}
    for nombre, descripcion in ROLES:
        rol, _ = Rol.objects.get_or_create(
            nombre=nombre,
            defaults={"descripcion": descripcion, "activo": True},
        )
        roles[nombre] = rol

    # Superusuario administrador
    admin, creado = User.objects.get_or_create(
        username="oswaldo",
        defaults={
            "email": "oswaldo@practica05.com",
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
            "password": make_password("Practica05Django"),
        },
    )
    if creado:
        PerfilUsuario.objects.get_or_create(
            usuario=admin,
            defaults={"rol": roles["Administrador"]},
        )

    # Usuarios de prueba con su rol
    for username, password, nombre_rol in USUARIOS:
        usuario, creado = User.objects.get_or_create(
            username=username,
            defaults={
                "is_active": True,
                "password": make_password(password),
            },
        )
        if creado:
            PerfilUsuario.objects.get_or_create(
                usuario=usuario,
                defaults={"rol": roles[nombre_rol]},
            )


def borrar_datos(apps, schema_editor):
    Rol = apps.get_model("usuarios", "Rol")
    PerfilUsuario = apps.get_model("usuarios", "PerfilUsuario")
    User = apps.get_model("auth", "User")
    usernames = ["oswaldo"] + [u[0] for u in USUARIOS]
    PerfilUsuario.objects.filter(usuario__username__in=usernames).delete()
    User.objects.filter(username__in=usernames).delete()
    Rol.objects.filter(nombre__in=[r[0] for r in ROLES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(cargar_datos, borrar_datos),
    ]
