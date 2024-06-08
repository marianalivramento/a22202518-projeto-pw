from django.shortcuts import render, redirect
from cursos.models import Curso
from cursos.models import Disciplina
from cursos.models import Projeto
from cursos.models import Docente
from .forms import DisciplinaForm, CursoForm, ProjetoForm, LinguagemForm, DocenteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models

# Create your views here.

def index_view(request):
    context = {
        'curso' : Curso.objects.first(),
        'disciplinas' : Disciplina.objects.all().order_by('ano', 'semestre', 'nome_da_disciplina'),
        'docentes' : Docente.objects.all().order_by('nome_do_docente')
    }
    return render(request, "cursos/index.html", context)

def contactos_view(request):
    return render(request, "cursos/contactos.html")

def disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id = disciplina_id)

    context = {
        'disciplina' : Disciplina.objects.get(id = disciplina_id),
        'projetos' : Projeto.objects.filter(disciplina = disciplina),
        'professor' : Docente.objects.filter(disciplinas = disciplina)
    }
    return render(request, "cursos/disciplina.html", context)

def projeto_view(request, projeto_id):
    context = {
        'projeto' : Projeto.objects.get(id = projeto_id)
    }
    return render(request, "cursos/projeto.html", context)

def professor_view(request, professor_id):
    context = {
        'professor' : Docente.objects.get(id = professor_id)
    }
    return render(request, "cursos/professor.html", context)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('login')

    return render(request, 'cursos/registo.html')

def logout_view(request):
    logout(request)
    return redirect('autenticacao:index')










@login_required

def nova_disciplina_view(request):
    form = DisciplinaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'cursos/nova_disciplina.html', context)

@login_required
def apaga_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('curso:index')

@login_required
def edita_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)

    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:index')
    else:
        form = DisciplinaForm(instance=disciplina)  # cria formulário com dados da instância autor

    context = {'form': form, 'disciplina':disciplina}
    return render(request, 'cursos/edita_disciplina.html', context)

@login_required
def edita_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)

    if request.POST:
        form = CursoForm(request.POST or None, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:index')
    else:
        form = CursoForm(instance=curso)  # cria formulário com dados da instância autor

    context = {'form': form, 'curso':curso}
    return render(request, 'cursos/edita_curso.html', context)

#----------------------------------------------------------------------------------------------------#

@login_required
def novo_projeto_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id= disciplina_id)
    form = ProjetoForm(request.POST or None, request.FILES)

    if form.is_valid():
        projeto = form.save(commit = False)
        projeto.disciplina = disciplina
        projeto.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'cursos/novo_projeto.html', context)

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('curso:index')

@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:index')
    else:
        form = ProjetoForm(instance=projeto)  # cria formulário com dados da instância autor

    context = {'form': form, 'projeto': projeto}
    return render(request, 'cursos/edita_projeto.html', context)

#----------------------------------------------------------------------------------------------------#

@login_required
def nova_linguagem_view(request):
    form = LinguagemForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'cursos/nova_linguagem.html', context)

#----------------------------------------------------------------------------------------------------#

@login_required
def novo_docente_view(request):
    form = DocenteForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'cursos/novo_docente.html', context)

@login_required
def apaga_docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    docente.delete()
    return redirect('curso:index')




