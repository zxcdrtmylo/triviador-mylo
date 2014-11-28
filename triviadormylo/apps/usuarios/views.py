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

def preguntas(request):
	if(request.method=="POST"):
		form=preguntas(request.POST)
		if(form.is_valid()):
			form.save()
	form=preguntas()
	return render_to_response("/Inicio/preguntas.html")
def registro_usuarios(request):
	if request.method=="POST":
		form=fusuario(request.POST)
		if(form.is_valid()):
			nuevo_usuario=request.POST['username']
			form.save()
			usuario=User.objects.get(username=nuevo_usuario)
			p=Perfil.objects.create(user=usuario)
			return HttpResponseRedirect("/Inicio/")
	else:
		form=fusuario()
	return render_to_response("usuario/registro.html",{"form":form},RequestContext(request))
def pagina_principal(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return HttpResponseRedirect("/Inicio/perfil/")
	form=AuthenticationForm()
	if request.method=="POST":
		form1=fusuario(request.POST)
		if(form1.is_valid()):
			nuevo_usuario=request.POST['username']
			form1.save()
			usuario=User.objects.get(username=nuevo_usuario)
			p=Perfil.objects.create(user=usuario)
			return HttpResponseRedirect("/Inicio/")
	else:
		form1=fusuario()
	return render_to_response("Inicio/principal.html",{"form":form,"form1":form1},RequestContext(request))
def login_usuario(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return HttpResponseRedirect("/Inicio/perfil/")
	form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form":form},RequestContext(request))
def perfil(request):
	return render_to_response("usuario/perfil.html",{'nombre':request.session["name"]},RequestContext(request))
def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/Inicio/")
def pagina_comentarios(request):
	if request.method=="POST":
		form=comentarios(request.POST)
		if(form.is_valid()):
			form.save()
	return render_to_response("Inicio/comentarios.html",{"comentarios":comentarios()},RequestContext(request))

def perfil_view(request):
	if request.user.is_authenticated():
		p=Perfil.objects.get(user=request.user)
		if request.method=="POST":
			form=fperfil(request.POST,request.FILES,instance=p)
			if form.is_valid:
				form.save()
				return HttpResponseRedirect("/Inicio/")
		else:
			form=fperfil()
		return render_to_response("usuario/perfil_add.html",{"form":form},RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")