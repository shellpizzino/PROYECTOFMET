from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="usuarios_usuario_set",
        blank=True,
        help_text="Los grupos a los que pertenece este usuario.",
        verbose_name="grupos",
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuarios_usuario_permissions_set",
        blank=True,
        help_text="Permisos específicos para este usuario.",
        verbose_name="permisos de usuario",
        related_query_name="usuario",
    )