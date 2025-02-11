from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import redirect

LISTA_ALUNOS = [
    {"nome": "João Silva", "matricula": "202301", "data_nascimento": "03/10/2009","curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Maria Oliveira", "matricula": "202302", "data_nascimento": "05/02/2008","curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Carlos Souza", "matricula": "202303", "data_nascimento": "20/12/2009","curso": "Técnico em Informática", "turma": "208"},
]
def listar_alunos(request):
    context={
        'lista': LISTA_ALUNOS,
    }
    return render(request, "listar_alunos.html", context)

def editar_aluno(request, indice):
    aluno = LISTA_ALUNOS[indice]  # Obtém a referência do aluno na lista


    if request.method == "POST":
        # Atualiza diretamente os valores do dicionário aluno
        aluno['nome'] = request.POST.get("nome")
        aluno['matricula'] = request.POST.get("matricula")
        aluno['curso'] = request.POST.get("curso")
        aluno['turma'] = request.POST.get("turma")


        return redirect('listar_alunos')  # Redireciona para a lista de alunos


    context = {
        'aluno': aluno,
        'indice': indice
    }
    return render(request, 'form_aluno.html', context)


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
        'rua': "Rua Domingos Borges", 
        'numero': 2367, 
        'bairro': "Santa Fé", 
        'cidade': "Teresina", 
        'estado': "Piauí", 
        'CEP': "*********",
    }
    return render(request,"dados.html",context)

def form(request):
    if request.method == "POST":
        nome=request.POST.get("nome")
        data_nascimento=request.POST.get("data_nascimento")
        rg=request.POST.get("rg")
        CPF=request.POST.get("CPF")
        telefone=request.POST.get("telefone")
        email=request.POST.get("email")
        rua=request.POST.get("rua")
        numero=request.POST.get("numero")
        bairro=request.POST.get("bairro")
        cidade=request.POST.get("cidade")
        estado=request.POST.get("estado")
        CEP=request.POST.get("CEP")
        
        context={
            "nome": nome,
            "data_nascimento": data_nascimento,
            "rg": rg,
            "CPF": CPF,
            "telefone": telefone,
            "email": email,
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "CEP": CEP,
        }
        
        return render(request,"dados.html",context)
    else:
        return render(request,"form.html")