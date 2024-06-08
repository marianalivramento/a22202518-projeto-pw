from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models, authenticate, login, logout
from bandas.models import Banda
import requests


def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('autenticacao:login')

    return render(request, 'autenticacao/registo.html')


def login_view(request):
    if request.method == "POST":

        # Verifica as credenciais
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            # Se as credenciais são válidas, faz login e redireciona
            login(request, user)
            return render(request, 'autenticacao/index.html')
        else:
            # Se inválidas, reenvia para login com mensagem
            render(request, 'autenticacao/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'autenticacao/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('autenticacao:index')

def index_view(request):
    url = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    url2 = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    response = requests.get(url)
    response2 = requests.get(url2)

    context = {
        'bandas': Banda.objects.all().order_by('nome_banda'),
        'previsao' : response.json(),
        'frases' : response2.json()
    }

    return render(request, "autenticacao/index.html", context)


