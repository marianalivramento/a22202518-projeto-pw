from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length = 100)
    info = models.TextField(blank = True)
    foto = models.ImageField(upload_to='blognest_fotos', null = True, blank = True)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length = 150)
    resumo = models.TextField(blank = True)
    texto = models.TextField(blank = True, null = True)
    link = models.URLField()
    data_de_publicacao = models.IntegerField(verbose_name = 'Data de Publicação')
    autor = models.ManyToManyField(Autor, related_name = 'artigo')
    #review = modes.ForeignKey(Review, on_delete = models.CASCADE, related_name = 'artigo', null = True)

    def __str__(self):
            return self.titulo

class Utilizador(models.Model):
    nome = models.CharField(max_length = 100)
    ano_de_inscricao = models.IntegerField(verbose_name = 'Ano de Inscrição')
    foto_de_perfil = models.ImageField(null = True)
    #reviews = models.ForeignKey(Review, on_delete = models.CASCADE, related_name = 'utilizador', null = True)

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    autor_do_comentario = models.OneToOneField(Utilizador, on_delete = models.CASCADE, related_name = 'comentario')
    artigo = models.ForeignKey(Artigo, on_delete = models.CASCADE, related_name = 'comentarios')
    texto = models.TextField(blank = True)

class Rating(models.Model):
    autor_do_rating = models.OneToOneField(Utilizador, on_delete = models.CASCADE, related_name = 'rating')
    artigo = models.ForeignKey(Artigo, on_delete = models.CASCADE, related_name = 'ratings')
    numero = models.IntegerField(blank= True, null = True)

class Review(models.Model):
    utilizador = models.ForeignKey(Utilizador, on_delete = models.CASCADE, related_name = 'review', null = True)
    preview_review = models.CharField(max_length = 150)
    artigo = models.ForeignKey(Artigo, on_delete = models.CASCADE, related_name = 'review')
    texto = models.TextField(blank = True)
    numero = models.IntegerField(null = True, validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])
    def __str__(self):
        return self.preview_review
