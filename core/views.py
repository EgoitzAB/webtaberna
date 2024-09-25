from django.views.generic import DetailView, TemplateView
from .models import Textos, Parrafos, ImagenAdicional
from django.http import FileResponse
import os
from django.views.decorators.http import require_GET
from django.http import HttpResponse


class HomeListView(DetailView):
    model = Textos
    template_name = 'core/home.html'
    context_object_name = 'vista'

    def get_object(self):
        # Recupera la vista "portada"
        return Textos.objects.get(nombre_vista="portada")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Recupera y ordena los párrafos asociados a la vista "portada"
        context['parrafos'] = self.object.parrafos_set.all().order_by('posicion')
        return context

def carta_pdf_view(request):
    # Ruta del archivo PDF
    pdf_path = os.path.join('static', 'pdfs', 'carta.pdf')

    # Abrir el archivo en modo lectura binaria
    pdf_file = open(pdf_path, 'rb')

    # Devolverlo como respuesta de archivo
    return FileResponse(pdf_file, content_type='application/pdf')

class NosotrosView(DetailView):
    model = Textos
    template_name = 'core/equipo.html'
    context_object_name = 'vista'
    
    def get_object(self):
        return Textos.objects.get(nombre_vista="nosotros")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener todos los párrafos asociados a la vista "nosotros"
        parrafos = Parrafos.objects.filter(vista=self.object).order_by('posicion')
        context['parrafos'] = parrafos
        
        # Obtener todas las imágenes principales y adicionales como objetos completos
        imagenes_principales = parrafos.exclude(imagen='').all()  # Párrafos con imágenes principales
        imagenes_adicionales = ImagenAdicional.objects.filter(parrafo__vista=self.object).all()  # Imágenes adicionales
        
        # Pasar las imágenes principales y adicionales al contexto
        context['imagenes_principales'] = imagenes_principales
        context['imagenes_adicionales'] = imagenes_adicionales
        
        return context
    

class PrivacyPolicyView(TemplateView):
    template_name = 'core/privacy_policy.html'

class TermsConditionsView(TemplateView):
    template_name = 'core/terminos_y_condiciones.html'
    

@require_GET
def robots_txt(request):
    file_path = os.path.join('static', 'robots.txt')
    with open(file_path, 'r') as f:
        return HttpResponse(f.read(), content_type="text/plain")