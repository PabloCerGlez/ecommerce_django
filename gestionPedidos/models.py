from django.db import models

# Create your models here.

class Clientes(models.Model):

     nombre=models.CharField(max_length=30)
     direccion=models.CharField(max_length=50, verbose_name="La dirección")
     email=models.EmailField(blank=True, null=True, verbose_name="El email")
     tfno=models.CharField(max_length=7)
     def __str__(self):
          return self.nombre
class Articulos(models.Model):
     nombre=models.CharField(max_length=30)
     seccion=models.CharField(max_length=20)
     precio=models.IntegerField()
     def __str__(self):
          return self.nombre
class Pedidos(models.Model):
     numero=models.IntegerField()
     fecha=models.DateField()
     entregado=models.BooleanField()
