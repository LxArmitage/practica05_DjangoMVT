from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.inicio,
        name="inicio"
    ),
    path(
        "login/",
        views.iniciar_sesion,
        name="login"
    ),
]
