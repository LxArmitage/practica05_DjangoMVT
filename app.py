# Punto de entrada WSGI para el despliegue (Render/gunicorn).
# Expone la aplicación de Django como "app" para que el comando por
# defecto "gunicorn app:app" funcione sin configuración adicional.
from practica05_DjangoMVT.wsgi import application as app
