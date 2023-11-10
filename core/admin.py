from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, tipoUsuario

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Login', {'fields': ('username','password','tipo_usuario')}),
        ('Información Personal', {'fields': ('first_name', 'last_name')}),
        ('Otros', {'fields': ('is_staff','is_superuser')})
    )

admin.site.register(tipoUsuario)