from django.shortcuts import render, redirect
from bandas.models import Banda
from bandas.models import Album
from bandas.models import Musica
from .forms import BandaForm
from .forms import AlbumForm
import requests

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

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

    return render(request, "bandas/index.html", context)

def lista_de_bandas_view(request):

    url = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    url2 = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    response = requests.get(url)
    response2 = requests.get(url2)

    context = {
        'bandas': Banda.objects.all().order_by('nome_banda'),
        'previsao' : response.json(),
        'frases' : response2.json()
    }

    return render(request, "bandas/lista-das-bandas.html", context)

def banda_view(request, banda_id):
    url = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    url2 = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    response = requests.get(url)
    response2 = requests.get(url2)

    context = {
        'banda': Banda.objects.get(id=banda_id),
        'previsao' : response.json(),
        'frases' : response2.json()

    }
    return render(request, "bandas/banda.html", context)



def album_view(request, album_id):
    url = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    url2 = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    response = requests.get(url)
    response2 = requests.get(url2)

    context = {
        'album': Album.objects.get(id=album_id),
        'previsao' : response.json(),
        'frases' : response2.json()

    }
    return render(request, "bandas/album.html", context)

def musica_view(request, musica_id):

    url = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    url2 = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    response = requests.get(url)
    response2 = requests.get(url2)

    context = {
        'musica': Musica.objects.get(id=musica_id),
        'previsao' : response.json(),
        'frases' : response2.json()

    }
    return render(request, "bandas/musica.html", context)

@login_required
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:index')

    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)


@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:index')
    else:
        form = BandaForm(instance=banda)  # cria formulário com dados da instância autor

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)  # Retrieve the Banda object using banda_id
    form = AlbumForm(request.POST or None, request.FILES)

    if form.is_valid():
        album = form.save(commit=False)  # cria objeto Livro sem gravar na base de dados
        album.banda = banda
        album.save()
        return redirect('bandas:index')

    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('autenticacao:index')

