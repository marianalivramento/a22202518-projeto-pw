from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'curso'

urlpatterns = [
    path('index/', views.index_view, name='index'),


    path('diciplina/<int:disciplina_id>', views.disciplina_view, name = 'disciplina'),
    path('projeto/<int:projeto_id>', views.projeto_view, name = 'projeto'),
    path('professor/<int:professor_id>', views.professor_view, name = 'professor'),

    path('contactos/', views.contactos_view, name = 'contactos'),

    path('registo/', views.registo_view, name="registo"),
    #path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('registar/', views.registo_view, name="registo"),

    path('disciplina/novo', views.nova_disciplina_view, name="nova_disciplina"),
    path('disciplina/<int:disciplina_id>/apaga', views.apaga_disciplina_view,name="apaga_disciplina"),
    path('disciplina/<int:disciplina_id>/edita', views.edita_disciplina_view,name="edita_disciplina"),

    path('curso/<int:curso_id>/edita', views.edita_curso_view,name="edita_curso"),

    path('projeto/novo/<int:disciplina_id>', views.novo_projeto_view, name="novo_projeto"),
    path('projeto/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),
    path('projeto/<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),

    path('projeto/disciplina/linguagem/novo', views.nova_linguagem_view, name="nova_linguagem"),

    path('disciplina/docente/novo', views.novo_docente_view, name="novo_docente"),
    path('docente/<int:docente_id>/apaga', views.apaga_docente_view,name="apaga_docente"),

]
