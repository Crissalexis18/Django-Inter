from django.urls import path
# from articulos import views, views_categoria
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'
# usuarios:logout
# usuarios:perfil

urlpatterns = [
    path('salir', LogoutView.as_view(), name='logout'),
    path('entrar', views.LoginView.as_view(), name='login'),
    path('registrar', views.RegistrarView.as_view(), name='registrar'),
    path('perfil/<int:pk>', views.EditarPerfilView.as_view(), name='perfil_editar'),
    path('perfil/nuevo', views.CrearPerfilView.as_view(), name='perfil_agregar'),
    path('perfil', views.PerfilView.as_view(), name='perfil'),
]
