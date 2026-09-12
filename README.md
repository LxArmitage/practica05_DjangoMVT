# Práctica 05 — Django MVT: Administración de usuarios

Aplicación web hecha con **Django (Modelo–Vista–Template)** y **SQLite3** para administrar
usuarios y roles de un negocio. Incluye inicio de sesión, mensaje de bienvenida según el rol
(con JavaScript), hoja de estilo CSS y el panel de administración de Django.

## Estructura del proyecto

```text
practica05_DjangoMVT/
├── manage.py
├── requirements.txt
├── render.yaml
├── practica05_DjangoMVT/        # configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── usuarios/                    # app de administración de usuarios
    ├── models.py               # Rol y PerfilUsuario
    ├── views.py                # inicio() e iniciar_sesion()
    ├── urls.py
    ├── admin.py
    ├── migrations/             # incluye datos iniciales (roles y usuarios)
    ├── templates/usuarios/     # inicio.html, login.html
    └── static/usuarios/css/    # estilos.css
```

## Base de datos y roles

Se usa **SQLite3** (BD nativa de Python). Modelos:

- **Rol**: `nombre`, `descripcion`, `activo`.
- **PerfilUsuario**: relaciona un `User` de Django (1 a 1) con un `Rol`.

Roles: Administrador, Especialista, Vendedor, Analista, Dueño y Cliente.

## Ejecutar en local

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir en el navegador:

- Inicio de sesión: http://127.0.0.1:8000/login/
- Panel de administración: http://127.0.0.1:8000/admin/

## Usuarios de prueba (se crean solos con las migraciones)

| Usuario                 | Contraseña        | Rol           |
|-------------------------|-------------------|---------------|
| admin                   | Practica05Django  | Administrador (superusuario) |
| rpizarroanalista        | probando          | Analista      |
| rpizarroduenio          | probando          | Dueño         |
| rpizarrovendedor        | probando          | Vendedor      |
| rpizarroespecialista    | probando          | Especialista  |
| rpizarrocliente         | probando          | Cliente       |

> Son cuentas de prueba para la práctica; la base de datos se recrea en cada despliegue.

## Despliegue en la nube (Render)

El archivo `render.yaml` deja lista la configuración. En un Web Service de Render:

- **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
- **Start Command:** `gunicorn practica05_DjangoMVT.wsgi:application`
- **Variables de entorno:** `DEBUG=False` y `SECRET_KEY` (valor propio).

Los archivos estáticos (CSS) se sirven con **WhiteNoise**.
