from django.contrib import admin
from .models import Textos, Parrafos, ImagenAdicional

class ImagenAdicionalInline(admin.TabularInline):
    model = ImagenAdicional
    extra = 1

class ParrafosAdmin(admin.ModelAdmin):
    inlines = [ImagenAdicionalInline]  # Incluye el inline para imágenes adicionales
    list_display = ('titulo', 'vista', 'posicion')  # Ajusta según las columnas que quieres mostrar

class ParrafosInline(admin.TabularInline):
    model = Parrafos
    extra = 1

class TextosAdmin(admin.ModelAdmin):
    inlines = [ParrafosInline]  # Incluye el inline para párrafos
    list_display = ('nombre_vista',)

# Registrar los modelos en el admin
admin.site.register(Textos, TextosAdmin)
admin.site.register(Parrafos, ParrafosAdmin)  # Registrar Parrafos con ParrafosAdmin
admin.site.register(ImagenAdicional)
