from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):	
	user=models.OneToOneField(User,unique=True)
	pais=models.CharField(max_length="30", null=False)
	ciudad=models.CharField(max_length="30", null=False)
	pasatiempo=models.CharField(max_length="50", null=False)
	color=models.CharField(max_length="30", null=False)
	mascota=models.CharField(max_length="30",null=False)
	avatar=ImageWithThumbsField(upload_to="img_user",sizes=((100,100),(200,200)))

class preguntas(models.Model):
	nombre=models.CharField(max_length=300)
	def __unicode__(self):
		return "->%s "%(self.nombre)

class comentarios(models.Model):
	contenido=models.TextField()
	fecha=models.DateField(auto_now=True)
	email=models.EmailField()
	usuario=models.ForeignKey(User)

class Tema(models.Model):
	nombre=models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.nombre

class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)
	def __str__(self):
		return self.nombre

class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respusta_opcional=models.CharField(max_length=500)
	respusta_opciona2=models.CharField(max_length=500)
	respusta_opciona3=models.CharField(max_length=500)
	respusta_opciona4=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta
class Sala(models.Model):
	usuario=models.ForeignKey(User)
	nombre=models.CharField(max_length=100)
	cantidad=models.IntegerField()
	tema=models.ManyToManyField(Tema,blank=True)