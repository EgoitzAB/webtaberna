from django.contrib import admin
from .models import Textos, Parrafos, Carta, CartaImagen

class ParrafosInline(admin.TabularInline):  # Puedes usar StackedInline en lugar de TabularInline si prefieres otra apariencia
    model = Parrafos
    extra = 1  # Número de formularios adicionales en blanco que se mostrarán

class TextosAdmin(admin.ModelAdmin):
    inlines = [ParrafosInline]

admin.site.register(Textos, TextosAdmin)

class CartaImagenInline(admin.TabularInline):
    model = CartaImagen
    extra = 1

class CartaAdmin(admin.ModelAdmin):
    inlines = [CartaImagenInline]

admin.site.register(Carta, CartaAdmin)