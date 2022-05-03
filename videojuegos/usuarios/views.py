from cProfile import Profile
from pyexpat import model
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm, FormDatosPersonales
from .models import DatosPersonales
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# from .forms import LoginForm

from usuarios.models import DatosPersonales
from usuarios.forms import FormDatosPersonales

from django.views import generic
from django.urls import reverse


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    # form_class = LoginForm


class RegistrarView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = "%(username)s se registró de manera exitosa"
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        
        return super().form_valid(form)

class CrearPerfilView(SuccessMessageMixin, CreateView):
    model = DatosPersonales
    form_class = FormDatosPersonales
    success_url = reverse_lazy('bienvenida')
    success_message = "Se guardaron tus datos personales"

    
    def form_valid(self, form):
        datos_personales = form.save(commit=False)
        datos_personales.user = self.request.user
        datos_personales.save()
        
        return super().form_valid(form)

class EditarPerfilView(SuccessMessageMixin, UpdateView):
    model = DatosPersonales
    # fields = '__all__'
    form_class = FormDatosPersonales
    success_url = reverse_lazy('bienvenida')
    success_message = "Se guardaron tus datos personales"

    extra_context = {'accion':'Modificar'}


class PerfilView(generic.RedirectView):

   def get_redirect_url(self):
       exists = DatosPersonales.objects.filter(user=self.request.user)
       if (exists):
            return reverse("perfil_editar", kwargs={'pk':self.request.user.datos.id})
       else:
            return reverse("perfil_agregar")
    
         
            
    










