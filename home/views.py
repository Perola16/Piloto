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

def dados(request):
    context={
        'nome': "Pérola",
        'data_nascimento': "05/10/2007",
        'rg': "*******",
        'CPF': "******",
        'telefone': "(89)98102-3839",
        'email': "perola.ppc@gmail.com",
        'endereco': "Rua Domingos Borges, 2367, Santa Fé, Teresina, Piauí,*********",
    }
    return render(request,"dados.html",context)

def form(request):
    if request.method == "POST":
        nome=request.POST.get("nome")
        idade=request.POST.get("idade")
        cidade=request.POST.get("cidade")
        
        context={
            "nome": nome,
            "idade": idade,
            "cidade": cidade,
        }
        
        return render(request,"dados.html",context)
    else:
        return render(request,"form.html")