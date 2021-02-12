from django.shortcuts import render,get_object_or_404
from .models import tecnico,cliente,orden
from django.core import serializers
from .form import tecnicoForm,clienteForm,ordenForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login

# Create your views here.

def base_layout(request):
	template='proyecto/index.html'
	return render(request,template)

def orden_detalle(request, pk):
    ordn = get_object_or_404(orden, pk=pk)
    return render(request, 'detalleorden.html', {'ordenn':ordn})

def index(request):
    tec = tecnico.objects.all()
    return render(request, 'login.html',{'tecnicos':tec})

def cliente_list(request):
    cli = cliente.objects.all()
    return render(request, 'vercliente.html',{'clientes':cli})

def admin(request):
    return render(request, 'index.html')

def tecnicoview(request):
    return render(request, 'indextecn.html')

def tecnico_nuevo(request):
    if request.method == 'POST':
        form = tecnicoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/administrador')
    else:
        form = tecnicoForm()
    return render(request, 'tecnico.html',{'form': form},)

def cliente_nuevo(request):
    if request.method == 'POST':
        form = clienteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/administrador')
    else:
        form = clienteForm()
    return render(request, 'cliente.html',{'form': form},)

def orden_nuevo(request):
    if request.method == 'POST':
        form = ordenForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/user/tecnico')
    else:
        form = ordenForm()
    return render(request, 'orden.html',{'form': form},)

def ver_orden(request):
    oorden = orden.objects.all()
    return render(request, 'verorden.html',{'ordenes':oorden})