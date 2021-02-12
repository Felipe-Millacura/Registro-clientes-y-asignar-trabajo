from django.db import models

# Create your models here.

class tecnico(models.Model):
	Idtecnico = models.CharField(max_length=3)
	NombreTecnico = models.CharField(max_length=100)
	Email = models.EmailField(max_length=100)
	Clave =	models.CharField(max_length=20)

	def __str__(self):
		return self.NombreTecnico

class cliente(models.Model):
	NombreCliente = models.CharField(max_length=100)
	Direccion = models.CharField(max_length=100)
	Ciudad = models.CharField(max_length=200,default="Seleccionar Ciudad")
	Comuna = models.CharField(max_length=200,default="Seleccionar Comuna")
	Telefono = models.CharField(max_length=9)
	Email = models.EmailField(max_length=100)
	TecnicoAsignado = models.ForeignKey(tecnico,on_delete=models.CASCADE)

	def __str__(self):
		return self.NombreCliente

class orden(models.Model):
	NombreCliente = models.CharField(max_length=100)
	FechaHoy = models.DateField()
	HoraInicio = models.TimeField()
	HoraTermino = models.TimeField()
	IDAscensor = models.CharField(max_length=3)
	Modelo = models.CharField(max_length=100)
	Fallas = models.TextField(max_length=1000)
	Reparaciones = models.TextField(max_length=1000)
	PiezasCambiadas = models.TextField(max_length=1000)
	TecnicoAsignado = models.ForeignKey(tecnico,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.NombreCliente
