from django.db import models

# Create your models here.

class Banda(models.Model):
    nome_banda = models.CharField(max_length = 200)
    nacionalidade = models.CharField(max_length = 50, null = True)
    ano_de_criacao = models.IntegerField(verbose_name = 'Ano de Criação', null = True)
    foto = models.ImageField(upload_to='banda_fotos', null = True, blank = True)
    estilo = models.CharField(max_length = 50, null = True)

    def __str__(self):
        return self.nome_banda


class Musica(models.Model):
    nome_musica = models.CharField(max_length = 200)
    duracao = models.IntegerField(verbose_name = 'Duração', null = True)
    link = models.URLField(null=True)
    data_lancamento = models.IntegerField(verbose_name = 'Lançamento', null = True)
    banda = models.ForeignKey(Banda, on_delete = models.CASCADE, related_name = 'nome_da_banda_na_musica', null = True)

    def __str__(self):
        return self.nome_musica


class Album(models.Model):
    nome_album = models.CharField(max_length = 200)
    capa = models.ImageField(upload_to="banda_fotos", null=True, blank=True, default=None)
    ano_de_lancamento = models.IntegerField(verbose_name = 'Ano de Lançamento')
    duracao_album = models.IntegerField(verbose_name = 'Duração', null = True)
    banda = models.ForeignKey(Banda, on_delete = models.CASCADE, related_name = 'albuns', null = True)
    musica = models.ManyToManyField(Musica, related_name = 'album')

    def __str__(self):
        return self.nome_album

