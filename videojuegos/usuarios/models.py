from django.db import models
from usuarios. validadores import rfc_validador, curp_validador
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class DatosPersonales(models.Model):
    rfc = models.CharField("R.F.C.", max_length=13, validators=[rfc_validador])
    curp = models.CharField("C.U.R.P.", max_length=18, validators=[curp_validador])
    direccion = models.CharField(_("Dirección"), max_length=150)
    telefono = models.CharField(_("Teléfono"), max_length=10)
    foto = models.ImageField(_('Foto'),upload_to='perfil')
    user = models.OneToOneField(User, verbose_name=_("Usuario"), related_name='datos', on_delete=models.DO_NOTHING)

