from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
	url(r'^$', pagina_principal),
	url(r'^comentarios/$', pagina_comentarios),
	url(r'^login/$', login_usuario),
	url(r'^logout/$', logout_usuario),
	url(r'^perfil/$', perfil),
	url(r'^perfil/add/$', perfil_view),
	url(r'^preguntas/$', preguntas),
	url(r'^blog/$', blog),
	url(r'^juego/$', juego),
	url(r'^registro/tema/$',registro_tema, name='Tema'),
    url(r'^tema/add/(\d+)/$',add_pregunta, name='agregar_pregunta'),
    url(r'^tema/edit/(\d+)/$',ver_preguntas, name='edit_pregunta'),
    url(r'^pregunta/edit/(\d+)/$',edit_pregunta, name='edit_pregunta'),
    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),
    url(r'^usuarios/$',ver_usuarios),
    url(r'^permisos/$',permisogeneral),
    url(r'^permiso/$',permiso),
)