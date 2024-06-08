from django.contrib import admin
from django.utils.html import format_html
from .models import Artigo
from .models import Autor
from .models import Utilizador
from .models import Comentario
from .models import Rating
from .models import Review

# Register your models here.

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo', 'autores')
    ordering = ('titulo', 'resumo', 'autor__nome')
    search_fields = ('titulo', 'resumo', 'autor__nome')

    def autores(self, obj):
        autores = obj.autor.all()
        if autores:
            first_autor = autores[0].nome
            if len(autores) > 1:
                return f"{first_autor}, et al."
            else:
                return first_autor
        return ""


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'info')
    ordering = ('nome', 'info')
    search_fields = ('nome', 'info')


class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_de_inscricao')
    ordering = ('nome', 'ano_de_inscricao')
    search_fields = ('nome', 'ano_de_inscricao')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('utilizador', 'artigo_titulo')
    ordering = ('autor_do_comentario__nome', 'artigo__titulo')
    search_fields = ('autor_do_comentario__nome', 'artigo__titulo')

    def artigo_titulo(self, obj):
        return obj.artigo.titulo


    def utilizador(self, obj):
        return obj.autor_do_comentario.nome

class RatingAdmin(admin.ModelAdmin):
    list_display = ('utilizador', 'artigo_titulo', 'numero')
    ordering = ('autor_do_rating__nome', 'artigo__titulo', 'numero')
    search_fields = ('autor_do_rating__nome', 'artigo__titulo', 'numero')

    def artigo_titulo(self, obj):
        return obj.artigo.titulo


    def utilizador(self, obj):
        return obj.autor_do_rating.nome

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('preview_review', 'utilizador', 'artigo_titulo', 'numero')
    ordering = ('preview_review', 'utilizador__nome', 'artigo__titulo', 'numero')
    search_fields = ('preview_review', 'utilizador_do_rating__nome', 'artigo__titulo', 'numero')

    def artigo_titulo(self, obj):
        return obj.artigo.titulo



admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Utilizador, UtilizadorAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Review, ReviewAdmin)
