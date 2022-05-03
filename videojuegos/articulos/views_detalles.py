from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from articulos.forms import FormCategoria, FormDetalleArticulos
from articulos.models import DetalleArticulos, Articulos
# from django.contrib.messages.views import SuccessMessageMixin, Fail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect



def ListaDetalles(request, pk):
    articulos = Articulos.objects.all()
    len(articulos)
    Articulos.objects.count()
    articulos = Articulos.objects.filter(id=pk)
    return render(request, 'articulos/detallearticulos_list.html', {'articulos': articulos})
    
class NuevoDetalleView(SuccessMessageMixin, CreateView):
    model = DetalleArticulos
    # fields = '__all__'
    form_class = FormDetalleArticulos
    success_url = reverse_lazy('bienvenida')

    def form_valid(self, form):
        return super().form_valid(form)


def Detalles(request):
    articulos = DetalleArticulos.objects.all()
    len(articulos)
    DetalleArticulos.objects.count()
    return render(request, 'articulos/detalles.html', {'articulos': articulos})

    

def EliminarDetalleView(request, pk):
    DetalleArticulos.objects.get(id=pk).delete()
    return redirect('detalles')


def EditarDetalleView(request, pk):
    articulo = DetalleArticulos.objects.get(id=pk)
    if request.method == 'POST':
        form = FormDetalleArticulos(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('detalles')
    else:
        form = FormDetalleArticulos(instance=articulo)
    return render(request, 'articulos/editar_detalle.html', {'form':form})
