from django.contrib import admin
from .models import Banda
from .models import Album
from.models import Musica

# Register your models here.

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome_banda', 'nacionalidade')
    ordering = ('nome_banda', 'nacionalidade')
    search_fields = ('nome_banda', 'nacionalidade')

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome_musica', 'data_lancamento')
    ordering = ('nome_musica', 'data_lancamento')
    search_fields = ('nome_musica', 'data_lancamento')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome_album', 'ano_de_lancamento')
    ordering = ('nome_album', 'ano_de_lancamento')
    search_fields = ('nome_album', 'ano_de_lancamento')

admin.site.register(Banda, BandaAdmin)
admin.site.register(Musica, MusicaAdmin)
admin.site.register(Album, AlbumAdmin)