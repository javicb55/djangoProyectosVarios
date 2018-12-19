# -*- coding: utf-8 -*-

import os.path
from django.conf.urls import *
from marcadores.views import *
from django.views.generic import TemplateView

site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
  #Navegador
  (r'^$', pagina_principal),
  (r'^usuario/(\w+)/$', pagina_usuario),
  #Gestión de sesiones
  (r'^login/$', 'django.contrib.auth.views.login'),
  (r'^logout/$', pagina_logout),
  (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': site_media }),
  (r'^registro/$', pagina_registro),
  (r'^registro/exitoso/$', TemplateView.as_view(template_name='registration/registro_exitoso.html')),
  #Cuenta de sesiones
  (r'^guardar/$', pagina_guardar_marcador),
)