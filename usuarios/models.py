from django.db import models
from django.contrib.auth.models import User


class Rol(models.Model):
    nombre = models.CharField(
        max_length=50,
        unique=True
    )
    descripcion = models.CharField(
        max_length=200,
        blank=True
    )
    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre


# ============================================================
# MODELO: PERFIL USUARIO
# Relaciona un usuario de Django con un rol
# ============================================================
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    rol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.rol.nombre}"
