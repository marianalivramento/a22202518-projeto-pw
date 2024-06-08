from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def saudacao_view(request, nome):
    return HttpResponse(f"Olá {nome}")         # -> http://22202518.pythonanywhere.com/noobsite/saudacao/mariana


def saudacao_view_2(request, nome, idade):
    return HttpResponse(f"Olá {nome}, tens {idade} anos")