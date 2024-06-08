from django.db import models

# Create your models here.

class Pessoa(models.Model):

    primeiro_nome = models.CharField(max_length = 200)
    segundo_nome = models.CharField(max_length = 200)
    idade = models.IntegerField()


    def __str__(self):
        return f'Primeiro nome: {self.primeiro_nome} | Segundo nome: {self.segundo_nome} | Idade: {self.idade}'

