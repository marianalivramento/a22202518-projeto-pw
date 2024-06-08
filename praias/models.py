from django.db import models

# Create your models here.


class Servico(models.Model):
    nome_servico = models.CharField(max_length = 200)
    #praia = models.ForeignKey(Praia, on_delete = models.CASCADE, related_name = 'serviço', null = True)

    def __str__(self):
        return self.nome_servico

class Praia(models.Model):
    nome = models.CharField(max_length = 200)
    foto = models.ImageField(upload_to='praia_fotos', null = True, blank = True)
    servicos = models.ManyToManyField(Servico, related_name = 'praia')

    def __str__(self):
        return self.nome

class Regiao(models.Model):
    nome_regiao = models.CharField(max_length = 200)
    #praia = models.ForeignKey(Praia, on_delete = models.CASCADE, related_name = 'regiao', null = True)
    praia = models.ManyToManyField(Praia, related_name = 'regiao')


