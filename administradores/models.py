from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The User must have a username')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Ensure the password is hashed
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # This will be stored hashed
    last_login = models.DateTimeField(null=True, blank=True)  # For tracking last login
    rol = models.CharField(max_length=50)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True)
    is_active = models.BooleanField(default=True)  # For active users
    is_staff = models.BooleanField(default=False)  # For staff permissions
    is_superuser = models.BooleanField(default=False)  # Superuser flag
    fecha_creacion = models.DateTimeField(default=timezone.now)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Additional required fields for superuser

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
