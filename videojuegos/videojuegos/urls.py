from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path

urlpatterns = [
    
]


urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('articulos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
