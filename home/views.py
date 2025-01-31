from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def sobre(request):
    return render(request,"sobre.html")

def contato(request):
    return render(request,"contato.html")

def localizacao(request):
    return render(request,"localizacao.html")

def ajuda(request):
    return render(request,"ajuda.html")

def exibiritem(request,id):
    return render(request,'exibiritem.html',{"id":id})

def perfil(request,usuario):
    return render(request,'perfil.html',{"usuario":usuario})