from django.db import models
from django.utils.translation import gettext_lazy as _

GENERO = [
    ('1', _('Acción')),
    ('2', _('Aventura')),
    ('3', _('Carrera')),
]

class Articulos(models.Model):
    nombre = models.CharField(_('nombre'), max_length=100)
    decripcion = models.TextField(_('Descripción'), null=True, blank=True)
    stock = models.IntegerField(_('stock'), default=0, null=True)
    genero = models.CharField(_('Género'), max_length=1, choices=GENERO)
    categoria = models.ForeignKey( "articulos.Categoria", verbose_name=_('Categoría'), on_delete=models.DO_NOTHING)
    detalles = models.ManyToManyField("articulos.DetalleArticulos", verbose_name=_('Imágenes de artículo'), related_name="imgDetalle", blank=True)
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(_('nombre'),max_length=100)
    descripcion = models.TextField(_('Descripción'), null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class DetalleArticulos(models.Model):
    nombre = models.CharField(_('nombre'), max_length=100)
    foto = models.ImageField(_('Foto'), upload_to='articulos')
    
    def __str__(self):
        return self.nombre



