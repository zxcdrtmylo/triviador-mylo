from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
	url(r'^$', pagina_principal),
	url(r'^comentarios/$', pagina_comentarios),
	url(r'^registro/$', registro_usuarios),
	url(r'^login/$', login_usuario),
	url(r'^logout/$', logout_usuario),
	url(r'^perfil/$', perfil),
	url(r'^perfil/add/$', perfil_view),
	url(r'^preguntas/$', preguntas),
)