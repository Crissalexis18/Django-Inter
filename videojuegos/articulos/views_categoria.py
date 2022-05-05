from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from articulos.forms import FormCategoria
from articulos.models import Articulos, Categoria
# from django.contrib.messages.views import SuccessMessageMixin, Fail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
import datetime


class ListaCategorias(ListView):
    model = Categoria
    # queryset = Categoria.objects.order_by('nombre')

class NuevaCategoriaView(CreateView):
    model = Categoria
    # fields = '__all__'
    form_class = FormCategoria
    success_url = reverse_lazy('categorias_lista')
    word = _('Nueva')
    extra_context = {'accion':word}

class EditarCategoriaView(UpdateView):
    model = Categoria
    # fields = '__all__'
    form_class = FormCategoria
    extra_context = {'accion':'Modificar'}
    
    success_url = reverse_lazy('categorias_lista')
    
class EliminarCategoriaView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias_lista')
    
    def form_valid(self, form):
        self.object = self.get_object()
        if Articulos.objects.filter(categoria=self.object):
            messages.error(self.request, 'No se pode eliminar la categoría; tiene artículos agregados')
            pass
        else:
            self.object.delete()
            messages.success(self.request, 'Se elimino con éxito la categoría')
        
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)  
    
class BienvenidaView(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hora'] = timezone.now()
        return context

    template_name = 'bienvenida.html'



