from django.views.generic import DetailView, TemplateView
from .models import Textos, Carta

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


class CartaView(TemplateView):
    template_name = 'pages/carta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cartas'] = Carta.objects.all()  # Obtén todas las cartas
        return context

class NosotrosView(TemplateView):
    template_name = 'core/equipo.html'