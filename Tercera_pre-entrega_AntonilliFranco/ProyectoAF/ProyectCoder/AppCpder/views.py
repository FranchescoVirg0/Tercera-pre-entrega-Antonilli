from django.shortcuts import render
from AppCpder.models import Consorcista, Administrador, Expensa
from django.http import HttpRequest, HttpResponse
from AppCpder.forms import *
from django.template.loader import get_template
# Create your views here.

def home(self):
    plantilla = get_template("index.html")
    return HttpResponse(plantilla.render())

def formulario(self):
    plantilla = get_template("formulario.html")
    return HttpResponse(plantilla.render())





class FormularioConsorcistaView(HttpRequest):

    def index(request):
        Consorcista = formularioConsorcista()
        return render(request, "ConsorcistaIndex.html", {"form":Consorcista})
    
    def procesar_formulario(request):
        consorcista = formularioConsorcista(request.POST)
        if consorcista.is_valid():
            consorcista.save()
            consorcista = formularioConsorcista()
        
        return render(request, "ConsorcistaIndex.html", {"form":consorcista, "mensaje":"OK"})
    
    def listar_consorcistas(request):
        consorcistas = Consorcista.objects.all()
        return render(request, "Listaconsorcistas.html", {"consorcistas": consorcistas})
    

class FormularioAdministradorView(HttpRequest):

    def index(request):
        Administrador = formularioAdministrador()
        return render(request, "AdministradorIndex.html", {"form":Administrador})
    
    def procesar_formulario(request):
        Administrador = formularioAdministrador(request.POST)
        if Administrador.is_valid():
            Administrador.save()
            Administrador = formularioAdministrador()
        
        return render(request, "AdministradorIndex.html", {"form":Administrador, "mensaje":"OK"})
    
    def listar_Administradores(request):
        Administradores = Administrador.objects.all()
        
        return render(request, "ListaAdministradores.html", {"Administradores": Administradores})
    
    
    
class FormularioExpensaView(HttpRequest):

    def index(request):
        Expensa = formularioExpensa()
        return render(request, "Expensaindex.html", {"form":Expensa})
    
    def procesar_formulario(request):
        Expensa = formularioExpensa(request.POST)
        if Expensa.is_valid():
            Expensa.save()
            Expensa = formularioExpensa()
        
        return render(request, "ExpensaIndex.html", {"form":Expensa, "mensaje":"OK"})
    
    def listar_Expensas(request):
        Expensas = Expensa.objects.all()
        return render(request, "ListaExpensas.html", {"Expensas": Expensas})
    
    