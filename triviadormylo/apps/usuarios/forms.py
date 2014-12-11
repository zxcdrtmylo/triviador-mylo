#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from captcha.fields import ReCaptchaField
import pdb
tipos=(('private','Privado'),('public','Publico'),('protected','Protegido'),)
class Captcha(forms.Form):
    	captcha = ReCaptchaField(attrs={'theme':'clean'})

class fperfil(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']

class fperfil_modificar(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']
		
class fusuario(UserCreationForm):
	username=forms.CharField(max_length=40,required=True,help_text=False,label="Nick")
	password2=forms.CharField(help_text=False,label="Confirmación", widget=forms.PasswordInput)
	first_name=forms.CharField(max_length=50,required=True,label="Nombre")
	last_name=forms.CharField(max_length=50,required=True,label="Apellido")
	email=forms.EmailField(max_length=100,required=True,label="Email")
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name","email")
	def save(self, commit=True):
		user=super(fusuario,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user
class ftema(ModelForm):
	class Meta:
		model=Tema
		exclude=['tema']

class fpregunta(ModelForm):
	nombre=forms.CharField(required=True,label="Pregunta :")
	class Meta:
		model=Pregunta
		exclude=['tema']

class frespuesta(ModelForm):
	class Meta:
		model=Respuesta
		exclude=['pregunta']

class SalaForms(ModelForm):
	tema=forms.ModelMultipleChoiceField(queryset=Tema.objects.all(), widget=forms.CheckboxSelectMultiple(), required=True)
	class Meta:
		model=Sala
		exclude=["usuario"]
class PermisoForm(ModelForm):
	class Meta:
		model=permiso
		exclude=[""]
class PermisosgeFoms(ModelForm):
	class Meta:
		model=permisogeneral
		exclude=[""]