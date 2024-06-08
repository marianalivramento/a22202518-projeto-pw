from cursos.models import Curso
from cursos.models import AreaCientifica
from cursos.models import Linguagem
from cursos.models import Disciplina
from cursos.models import Docente
from cursos.models import Projeto
import json

Curso.objects.all().delete()
AreaCientifica.objects.all().delete()
Linguagem.objects.all().delete()
Disciplina.objects.all().delete()
Docente.objects.all().delete()
Projeto.objects.all().delete()


with open('cursos/json/cursos.json') as f:
    cursos = json.load(f)

    for curso in cursos:
        Curso.objects.create(
                nome_do_curso = curso['nome_do_curso'],
                abreviatura = curso['abreviatura'],
                apresentacao = curso['apresentacao'],
                objetivos = curso['objetivos'],
                competencias = curso['competencias'],
                grau = curso['grau'],
                numero_de_semestres = curso['numero_de_semestres'],
                numero_de_creditos = curso['numero_de_creditos'],
            )

with open('cursos/json/area_cientifica.json') as f:
    areas = json.load(f)

    for area in areas:
        AreaCientifica.objects.create(
                nome_da_area = area['nome_da_area']
            )


with open('cursos/json/linguagens.json') as f:
    linguagens = json.load(f)

    for linguagem in linguagens:
        Linguagem.objects.create(
                nome_da_linguagem = linguagem['nome_da_linguagem']
            )


with open('cursos/json/disciplinas.json') as f:
    disciplinas = json.load(f)

    for disciplina in disciplinas:

        new_disciplina = Disciplina.objects.create(
                nome_da_disciplina = disciplina['nome_da_disciplina'],
                ano = disciplina['ano'],
                semestre = disciplina['semestre'],
                ects = disciplina['ects'],
                curricularIUnitReadableCode = disciplina['curricularIUnitReadableCode']
            )

        for area_data in disciplina['area_cientifica']:
            #try:
                #area_d = AreaCientifica.objects.get(nome_da_area = area_data['area'])
            #except AreaCientifica.DoesNotExist:
            area_d = AreaCientifica.objects.create(nome_da_area = area_data)

            new_disciplina.area_cientifica = area_d

        for linguagem in disciplina['linguagens']:
            #try:
               # linguagem_d = Linguagem.objects.get(nome_da_linguagem = linguagem)
            #except Linguagem.DoesNotExist:
            linguagem_d = Linguagem.objects.create(nome_da_linguagem = linguagem)

            new_disciplina.linguagens.add(linguagem_d)

# bro aqui está mal, mas não consigo que o try except funcione

with open('cursos/json/docentes.json') as f:
    docentes = json.load(f)

    for docente in docentes:
        new_docente = Docente.objects.create(
                nome_do_docente = docente['nome_do_docente']
            )

    for disciplina_data in docente['disciplinas']:

        disciplina_d = Disciplina.objects.get(nome_da_disciplina = disciplina_data['disciplina'])

        if disciplina_d is not None:
            new_docente.disciplinas.add(disciplina_d)


with open('cursos/json/projeto.json') as f:
    projetos = json.load(f)

    for projeto in projetos:
        new_projeto = Projeto.objects.create(
                nome_do_projeto = projeto['nome_do_docente'],
                descricao = projeto['descricao']
            )

    for linguagem_data in projeto['linguagens']:

        linguagem_d = Linguagem.objects.get(nome_da_linguagem = linguagem_data['linguagem'])

        if linguagem_d is not None:
            new_projeto.linguagens.add(linguagem_d)








