from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import pdb

def eliminar_pregunta(request,id):
	menu=permisos(request)
	if request.user.is_authenticated():
		pregunta=Pregunta.objects.get(id=int(id))
		id=pregunta.tema.id
		respuesta=Respuesta.objects.get(pregunta=pregunta)
		pregunta.delete()
		respuesta.delete()
		return HttpResponseRedirect("/Inicio/tema/edit/"+str(id)+"/")
	else:
		return HttpResponseRedirect("/Inicio/login/")
def edit_pregunta(request,id):
	menu=permisos(request)
	if request.user.is_authenticated():
		pregunta=Pregunta.objects.get(id=int(id))
		respuesta=Respuesta.objects.get(pregunta=pregunta)
		titulo="Editar pregunta"
		titulo2="Editar las respuestas"
		if request.method=="POST":
			formulario=fpregunta(request.POST,instance=pregunta)
			formulario2=frespuesta(request.POST,instance=respuesta)
			if formulario.is_valid() and formulario2.is_valid():
				formulario.save()
				formulario2.save()
				estado=True
				datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2,'menu':menu}
				return render_to_response("Inicio/registro_preguntas.html",datos,context_instance=RequestContext(request))
		else:
			formulario=fpregunta(instance=pregunta)
			formulario2=frespuesta(instance=respuesta)
		datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2,'menu':menu}
		return render_to_response("Inicio/registro_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")
def ver_preguntas(request,id):
	menu=permisos(request)
	if request.user.is_authenticated():
		tema=Tema.objects.get(id=int(id))
		preguntas=Pregunta.objects.filter(tema=tema)
		datos={'tema':tema,'preguntas':preguntas,'menu':menu}
		return render_to_response("Inicio/ver_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")
def ver_usuarios(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		usuarios=User.objects.all()
		#tema=Tema.objects.get(id=int(id))
		#preguntas=Pregunta.objects.filter(tema=tema)
		datos={'usuarios':usuarios,'menu':menu}
		return render_to_response("Inicio/usuarios.html",datos,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")
def add_pregunta(request,id):
	menu=permisos(request)
	if request.user.is_authenticated():
		tema=Tema.objects.get(id=int(id))
		titulo="Registrar pregunta para el tema de "+tema.nombre
		titulo2="Registre las respuestas"
		if request.method=="POST":
			formulario=fpregunta(request.POST)
			formulario2=frespuesta(request.POST)
			if formulario.is_valid() and formulario2.is_valid():
				pregunta=formulario.save(commit=False)
				pregunta.tema=tema
				pregunta.save()
				respuesta=formulario2.save(commit=False)
				respuesta.pregunta=pregunta
				respuesta.save()
				estado=True
				formulario=fpregunta()
				datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2,'menu':menu}
				return render_to_response("Inicio/registro_preguntas.html",datos,context_instance=RequestContext(request))
		else:
			formulario=fpregunta()
			formulario2=frespuesta()
		datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2,'menu':menu}
		return render_to_response("Inicio/registro_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")
def registro_tema(request):
	menu=permisos(request)
	usuario=request.user
	if not usuario.has_perm("usuarios.add_tema"):
		est=True
		men="Udted no tiene los permisos requeridos"
		dat={'est':est,'men':men,'menu':menu}
		return render_to_response("Inicio/registro_temas.html",dat,context_instance=RequestContext(request))
	if request.user.is_authenticated():
		titulo="Regitro de temas"
		temas=Tema.objects.all()
		if request.method=="POST":
			formulario=ftema(request.POST)
			if formulario.is_valid():
				formulario.save()
				estado=True
				datos={'titulo':titulo,'formulario':formulario,'estado':estado,'temas':temas,'menu':menu}
				return render_to_response("Inicio/registro_temas.html",datos,context_instance=RequestContext(request))
		else:
			formulario=ftema()
		datos={'titulo':titulo,'formulario':formulario,'temas':temas,'menu':menu}
		return render_to_response("Inicio/registro_temas.html",datos,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")
def juego(request):
	menu=permisos(request)
	if request.user.is_authenticated():	
		if request.method=="POST":
			form12=SalaForms()
			if form12.is_valid():
				form12.save()
			return render_to_response("Inicio/juego.html",{'form12':form12,'menu':menu},RequestContext(request))
		else:
			form12=SalaForms()
		return render_to_response("Inicio/juego.html",{'form12':form12,'menu':menu},RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")
def blog(request):
	menu=permisos(request)
	return render_to_response("Inicio/blog.html",{'menu':menu},RequestContext(request))

def preguntas(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		if(request.method=="POST"):
			form=preguntas(request.POST)
			if(form.is_valid()):
				form.save()
		form=preguntas()
		return render_to_response("/Inicio/preguntas.html",{'menu':menu},RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")
def pagina_principal(request):
	menu=permisos(request)
	if request.method=="POST":
		form1=fusuario(request.POST)
		if(form1.is_valid()):
			nuevo_usuario=request.POST['username']
			form1.save()
			usuario=User.objects.get(username=nuevo_usuario)
			p=Perfil.objects.create(user=usuario)
			return HttpResponseRedirect("/Inicio/login/")
	else:
		form1=fusuario()
	return render_to_response("Inicio/principal.html",{"form1":form1,'menu':menu},RequestContext(request))
def login_usuario(request):
	menu=permisos(request)
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if request.session['contador']>2:
			form2=Captcha(request.POST)
			if form2.is_valid():
				pass
			else:
				datos={"form":form,"form2":form2,'menu':menu}
				return render_to_response("usuario/login.html",datos,RequestContext(request))
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado is not None:
				if resultado.is_active:
					login(request, resultado)
					#del request.session['contador']
					return HttpResponseRedirect("/Inicio/perfil/")
				else:
					login(request, resultado)
					return HttpResponseRedirect("/Inicio/perfil/")
			else:
				request.session['contador']=request.session['contador']+1
				aux=request.session['contador']
				estado=True
				mensaje="Error en los datos"+ str(aux)
				if aux>2:
					form2=Captcha()
					datos={"form":form,"form2":form2, "estado":estado, "mensaje":mensaje,'menu':menu}
				else:
					datos={"form":form, "estado":estado, "mensaje":mensaje,'menu':menu}
				return render_to_response("usuario/login.html",datos,RequestContext(request))		
	else:
		request.session['contador']=0		
		form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form":form,'menu':menu},RequestContext(request))
def perfil(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		return render_to_response("usuario/perfil.html",{'menu':menu},RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")	
def logout_usuario(request):
	menu=permisos(request)
	logout(request)
	return HttpResponseRedirect("/Inicio/")
def pagina_comentarios(request):
	menu=permisos(request)
	if request.method=="POST":
		form=comentarios(request.POST)
		if(form.is_valid()):
			form.save()
	return render_to_response("Inicio/comentarios.html",{"comentarios":comentarios(),'menu':menu},RequestContext(request))

def perfil_view(request):
	menu=permisos(request)
	if request.user.is_authenticated():
		usu=request.user
		usuario=User.objects.get(username=usu)
		perfil=Perfil.objects.get(user=usuario)
		if request.method=="POST":
			form=fperfil(request.POST,request.FILES, instance=perfil)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect("/Inicio/perfil/")
		else:
			form=fperfil(instance=perfil)
		return render_to_response("usuario/perfil_add.html", {"form":form,'menu':menu},RequestContext(request))
	else:
		return HttpResponseRedirect("/Inicio/login/")

def permisos(request):
	listapermisos=[]
	if request.user.has_perm("usuarios.add_tema"):
		listapermisos.append({"url":"/Inicio/registro/tema/","label":"ADD TEMAS"})
	return listapermisos
