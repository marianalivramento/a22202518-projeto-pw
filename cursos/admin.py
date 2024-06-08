from django.contrib import admin
from .models import Curso
from .models import AreaCientifica
from .models import Disciplina
from .models import Linguagem
from .models import Projeto
from .models import Docente

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_do_curso','codigo_do_curso','grau')
    ordering = ('nome_do_curso','codigo_do_curso', 'grau')
    search_fields = ('nome_do_curso','codigo_do_curso', 'grau')

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome_da_area',)
    ordering = ('nome_da_area',)
    search_fields = ('nome_da_area',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome_da_disciplina', 'ano', 'semestre', 'ects', 'curricularIUnitReadableCode')
    ordering = ('nome_da_disciplina', 'ano', 'semestre', 'ects', 'curricularIUnitReadableCode')
    search_fields = ('nome_da_disciplina', 'ano', 'semestre', 'ects', 'curricularIUnitReadableCode')

class LinguagemAdmin(admin.ModelAdmin):
    list_display = ('nome_da_linguagem',)
    ordering = ('nome_da_linguagem',)
    search_fields = ('nome_da_linguagem',)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome_do_projeto', 'descricao')
    ordering = ('nome_do_projeto', 'descricao')
    search_fields = ('nome_do_projeto', 'descricao')

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome_do_docente','display_disciplinas')
    ordering = ('nome_do_docente',)
    search_fields = ('nome_do_docente',)

    def display_disciplinas(self, obj):
        return ", ".join([disciplina.nome_da_disciplina for disciplina in obj.disciplinas.all()])
        display_disciplinas.short_description = 'Disciplinas'

admin.site.register(Curso, CursoAdmin)
admin.site.register(AreaCientifica, AreaCientificaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Linguagem, LinguagemAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Docente, DocenteAdmin)