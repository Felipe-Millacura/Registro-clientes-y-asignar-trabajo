from django import forms
from .models import tecnico,cliente,orden

class tecnicoForm(forms.ModelForm):
    class Meta:
        model=tecnico
        widgets = {
        'Clave': forms.PasswordInput(),}
        fields=('Idtecnico','NombreTecnico','Email','Clave')

class clienteForm(forms.ModelForm):
    class Meta:
        model=cliente
        fields=('NombreCliente','Direccion','Ciudad','Comuna','Telefono','Email','TecnicoAsignado')

class ordenForm(forms.ModelForm):
    class Meta:
        model=orden
        fields=('NombreCliente','FechaHoy','HoraInicio','HoraTermino','IDAscensor','Modelo','TecnicoAsignado','Fallas','Reparaciones','PiezasCambiadas')