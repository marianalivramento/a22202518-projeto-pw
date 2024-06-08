from django import template

register = template.Library()

@register.filter
def albuns_ordenados(banda):
    return banda.albuns.all().order_by('ano_de_lancamento')

@register.filter
def musicas_ordenadas(album):
    return album.musica.all().order_by('nome_musica')