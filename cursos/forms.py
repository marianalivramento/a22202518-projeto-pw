from django import forms    # formulários Django
from .models import Disciplina
from .models import Curso
from .models import Projeto
from .models import Linguagem
from .models import Docente


class DisciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina       # classe para a qual é o formulário
    fields = ['nome_da_disciplina', 'ano', 'semestre', 'ects', 'curricularIUnitReadableCode', 'linguagens']

    widgets = {
        'nome_da_disciplina': forms.TextInput(attrs={
          'placeholder':'Nome da disciplina',
      }),
        'ano': forms.NumberInput(attrs={
            'type': 'number',  # This sets the input type to number
            'min': '1',     # Example minimum value
            'max': '3'     # Example maximum value
        })
    }


class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso      # classe para a qual é o formulário
    fields = ['nome_do_curso', 'codigo_do_curso', 'apresentacao', 'objetivos', 'competencias', 'grau', 'numero_de_semestres', 'numero_de_creditos']

    labels = {
        'apresentacao' : 'Apresentação',
        'competencias' : 'Competências',
    }

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto      # classe para a qual é o formulário
    fields = ['nome_do_projeto', 'descricao', 'conceitos_aplicados', 'tecnologias_usadas', 'imagem', 'linguagens']

    labels = {
        'descricao' : 'Descrição',
    }

class LinguagemForm(forms.ModelForm):
    class Meta:
        model = Linguagem
        fields = ['nome_da_linguagem']

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'