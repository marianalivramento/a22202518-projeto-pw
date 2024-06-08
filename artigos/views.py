from django.shortcuts import render, redirect
from artigos.models import Artigo, Autor, Review, Utilizador
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.decorators import login_required
from .forms import ArtigoForm, ReviewForm, AutorForm


def index_view(request):
    context = {
        'artigos' : Artigo.objects.all().order_by('titulo'),
    }

    return render(request, "artigos/index.html", context)


def artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    context = {
        'artigo' : Artigo.objects.get(id= artigo_id),
        'autor' : Autor.objects,
        'reviews' : Review.objects.filter(artigo=artigo)

    }

    return render(request, "artigos/artigo.html", context)

def autor_view(request, autor_id):
    context = {
        'autor' : Autor.objects.get(id= autor_id)
    }

    return render(request, "artigos/autor.html", context)

def autores_view(request):
    context = {
        'autores': Autor.objects.all()
    }

    return render(request, "artigos/autores.html", context)

def review_view(request, review_id):
    context = {
        'review' : Review.objects.get(id = review_id)
    }

    return render(request, "artigos/review.html", context)

def utilizador_view(request, utilizador_id):
    context = {
        'utilizador' : Utilizador.objects.get(id = utilizador_id)
    }

    return render(request, "artigos/utilizador.html", context)


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

    return render(request, 'artigos/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('artigos:index')
        else:
            render(request, 'artigos/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'artigos/login.html')

def logout_view(request):
    logout(request)
    return redirect('autenticacao:index')

@login_required
def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:index')

    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@login_required
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:index')
    else:
        form = ArtigoForm(instance=artigo)  # cria formulário com dados da instância artigo

    context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/edita_artigo.html', context)


@login_required
def apaga_review_view(request, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return redirect('artigos:index')

@login_required
def nova_review_view(request):
    form = ReviewForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:index')

    context = {'form': form}
    return render(request, 'artigos/nova_review.html', context)

@login_required
def edita_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)

    if request.POST:
        form = AutorForm(request.POST or None, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:index')
    else:
        form = AutorForm(instance=autor)  # cria formulário com dados da instância artigo

    context = {'form': form, 'autor': autor}
    return render(request, 'artigos/edita_autor.html', context)
