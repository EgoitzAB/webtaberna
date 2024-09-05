from django.db import models
from PIL import Image, ImageOps

class Textos(models.Model):
    nombre_vista = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_vista

class Parrafos(models.Model):
    vista = models.ForeignKey(Textos, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    posicion = models.IntegerField(blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='parrafos_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Parrafos, self).save(*args, **kwargs)
        if self.imagen:
            # Abrir la imagen
            img = Image.open(self.imagen.path)
            max_size = (800, 600)
            # Redimensionar la imagen
            img.thumbnail(max_size, Image.Resampling.LANCZOS)

            # Transponer la imagen para eliminar EXIF
            img_without_exif = ImageOps.exif_transpose(img)
            # Guardar la imagen con calidad optimizada
            img_without_exif.save(self.imagen.path, quality=90, optimize=True)


class Carta(models.Model):
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.idioma

class CartaImagen(models.Model):
    carta = models.ForeignKey(Carta, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='cartas/')
    indice = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.carta.idioma} - Imagen {self.indice}"
