from django.http import HttpResponse
from django.shortcuts import render, redirect

from articulos.models import Articulos, Categoria
from articulos.forms import FormArticulo
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.translation import gettext as _

#TimeZone Configuracion
# Prepare a map of common locations to timezone choices you wish to offer.
common_timezones = {
    'London': 'Europe/London',
    'Paris': 'Europe/Paris',
    'New York': 'America/New_York',
    'Mexico City': 'America/Mexico_City',
}

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'zona.html', {'timezones': common_timezones, 
            })

# select * from Entry where headline like '%What%'

def palabras(request):
    sentencia = 'Bienvenido a mi sitio'
    words = ['Bienvenido','a','mi','sitio.']
    salida = _(sentencia)
    output = _(' '.join(words))

    return HttpResponse(output)


# URLConf->MVT
#@permission_required('add_articulos')
def lista_articulos(request):
    articulos = Articulos.objects.all()
    # articulos = Articulos.objects.order_by('-stock','nombre')
    # articulos = Articulos.objects.filter(categoria__nombre='Aventura')
    print(articulos.query)
    len(articulos)
    Articulos.objects.count()
    #select * from articulos_articulos;
    
    return render(request, 'articulos.html', {'articulos': articulos})


def eliminar_articulos(request, id):
    Articulos.objects.get(id=id).delete()
    return redirect('articulos_lista')


# def eliminar_categoria(request, id):
#     context = {}
#     # categoria = Categoria.objects.get(id=id)
#     # articulos = Articulos.objects.filter(categoria=categoria)
#     articulos = Articulos.objects.filter(categoria_id=id)
#     if articulos:
        
#     else:
        
#     try:
#         Categoria.objects.get(id=id).delete()
#     except :
#         context['error'] = 'No se puede eliminar una categoria que tiene articulos'
        
#     return redirect('articulos_lista',context)

@login_required
def nuevo_articulo(request):
    if request.method == 'POST':
        form = FormArticulo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos_lista')
    else:
        form = FormArticulo()
    return render(request, 'nuevo_articulo.html', {'form':form})


def editar_articulos(request, id):
    articulo = Articulos.objects.get(id=id)
    if request.method == 'POST':
        form = FormArticulo(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('articulos_lista')
    else:
        form = FormArticulo(instance=articulo)
    return render(request, 'editar_articulo.html', {'form':form})




    