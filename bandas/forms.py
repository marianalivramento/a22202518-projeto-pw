from django import forms    # formulários Django
from .models import Banda
from .models import Album

class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Banda.

    help_texts = {
      'ano_de_criacao': 'ano de formação da banda',
      'foto': 'formats allwoed: png / jpeg',
    }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nome_album', 'capa', 'ano_de_lancamento', 'duracao_album']