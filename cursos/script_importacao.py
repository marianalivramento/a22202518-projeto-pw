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


with open('cursos/json/lei.json') as f:
    data = json.load(f)

    if 'courseFlatPlan' in data:
        course_flat_plan = data['courseFlatPlan']

        for disciplina_data in course_flat_plan:
            new_disciplina = Disciplina.objects.create(
                nome_da_disciplina=disciplina_data['curricularUnitName'],
                ano=disciplina_data['curricularYear'],
                semestre=disciplina_data['semester'],
                ects=disciplina_data['ects'],
                curricularIUnitReadableCode=disciplina_data['curricularIUnitReadableCode']
            )

    if 'courseDetail' in data:
        course_details = data['courseDetail']

        new_curso = Curso.objects.create(
            nome_do_curso=course_details['courseName'],
            codigo_do_curso = course_details['courseCode'],
            apresentacao=course_details['presentation'],
            objetivos=course_details['objectives'],
            competencias=course_details['competences'],
            grau=course_details['conferedDegree'],
            numero_de_semestres=course_details['semesters'],
            numero_de_creditos=course_details['courseECTS']
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
                descricao = projeto['descricao'],
                conceitos_aplicados = projeto['conceitos_aplicados'],
                tecnologias_usadas = projeto['tecnologias_usadas']
            )

    for linguagem_data in projeto['linguagens']:

        linguagem_d = Linguagem.objects.get(nome_da_linguagem = linguagem_data['linguagem'])

        if linguagem_d is not None:
            new_projeto.linguagens.add(linguagem_d)





