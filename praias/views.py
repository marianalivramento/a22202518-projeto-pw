from django.shortcuts import render
from praias.models import Praia
from praias.models import Regiao
from praias.models import Servico

# Create your views here.


def index_view(request):
    context = {
        'praias': Praia.objects.all().order_by('nome'),
        'servicos': Servico.objects.all(),
        'regioes': Regiao.objects.all().order_by('-nome_regiao'),
    }

    return render(request, "praias/index.html", context)

def praia_view(request, praia_id):
    context = {
        'praia': Praia.objects.get(id= praia_id),
    }

    return render(request, "praias/praia.html", context)
