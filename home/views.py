from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("A view index funcionou, Wow!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim</h1>")