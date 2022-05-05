from django.urls import path
from articulos import views, views_categoria, views_detalles


urlpatterns = [
    path('', views_categoria.BienvenidaView.as_view(), name='bienvenida'),

    path('zona', views.set_timezone, name='zona_horaria'),
    path('palabras', views.palabras, name='palabras'),
    
    path('articulos', views.lista_articulos, name='articulos_lista'),
    path('articulos/nuevo', views.nuevo_articulo, name='nuevo_articulo'),
    path('articulos/eliminar/<int:id>', views.eliminar_articulos, name='eliminar_articulos'),
    path('articulos/editar/<int:id>', views.editar_articulos, name='editar_articulos'),
    
    path('categorias', views_categoria.ListaCategorias.as_view(), name='categorias_lista'),
    path('categorias/nuevo', views_categoria.NuevaCategoriaView.as_view(), name='nueva_categoria'),
    path('categorias/editar/<int:pk>', views_categoria.EditarCategoriaView.as_view(), name='editar_categoria'),
    path('categorias/eliminar/<int:pk>', views_categoria.EliminarCategoriaView.as_view(), name='eliminar_categoria'),

    path('detalles/<int:pk>', views_detalles.ListaDetalles, name='detalles_lista'),
    path('detalles/nuevo', views_detalles.NuevoDetalleView.as_view(), name='nuevo_detalle'),
    path('detalle', views_detalles.Detalles, name='detalles'),
    path('detalle/editar/<int:pk>', views_detalles.EditarDetalleView, name='editar_detalle'),
    path('detalle/eliminar/<int:pk>', views_detalles.EliminarDetalleView, name='eliminar_detalle'),
]
