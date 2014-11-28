from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):	
	user=models.OneToOneField(User,unique=True)
	pais=models.CharField(max_length="30", null=False)
	avatar=ImageWithThumbsField(upload_to="img_user",sizes=((50,50),(200,200)))

class preguntas(models.Model):
	nombre=models.CharField(max_length=300)
	def __unicode__(self):
		return "->%s "%(self.nombre)

class comentarios(models.Model):
	contenido=models.TextField()
	fecha=models.DateField(auto_now=True)
	email=models.EmailField()
	usuario=models.ForeignKey(User)

