from django.db import models

# Create your models here.

class AreaCientifica(models.Model):
    nome_da_area = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome_da_area


class Linguagem(models.Model):
    nome_da_linguagem = models.CharField(max_length = 10)

    def __str__(self):
        return self.nome_da_linguagem



class Disciplina(models.Model):
    nome_da_disciplina = models.CharField(max_length = 50)
    ano = models.IntegerField(verbose_name = 'Ano da disciplina')
    semestre = models.CharField(max_length = 50)
    ects = models.IntegerField(verbose_name = 'Número de ects')
    curricularIUnitReadableCode = models.CharField(max_length = 50)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete = models.CASCADE, related_name = 'disciplina', null = True)
    linguagens = models.ManyToManyField(Linguagem, related_name = 'disciplina', blank = True, null = True)
    apresentacao = models.TextField(null= True, blank = True)
    #curso = models.ForeignKey(Curso, on_delete = models.CASCADE, related_name = 'disciplina', null = True)

    def __str__(self):
        return self.nome_da_disciplina


class Curso(models.Model):
    nome_do_curso = models.CharField(max_length = 50)
    codigo_do_curso = models.IntegerField(verbose_name = 'Código do curso', null = True)
    #abreviatura = models.CharField(max_length = 20)
    apresentacao = models.TextField(blank = True)
    objetivos = models.TextField(blank = True)
    competencias = models.TextField(blank = True)
    grau = models.CharField(max_length = 50)
    numero_de_semestres = models.IntegerField(verbose_name = 'Número de semestres')
    numero_de_creditos = models.IntegerField(verbose_name = 'Número de créditos')
    disciplinas = models.ForeignKey(Disciplina, on_delete = models.CASCADE, related_name = 'curso', null = True)


    def __str__(self):
        return self.nome_do_curso


class Docente(models.Model):
    nome_do_docente = models.CharField(max_length = 50)
    disciplinas = models.ManyToManyField(Disciplina, related_name = 'docentes')
    foto = models.ImageField(upload_to='curso_fotos', null = True, blank = True)

    def __str__(self):
        return self.nome_do_docente

class Projeto(models.Model):
    nome_do_projeto = models.CharField(max_length = 50)
    descricao = models.TextField(blank = True)
    conceitos_aplicados = models.TextField(blank = True, null = True)
    tecnologias_usadas = models.TextField(blank = True, null = True)
    imagem = models.ImageField(null = True, blank = True)
    link_youtube = models.URLField(null=True, blank = True)
    link_github = models.URLField(null=True, blank = True)
    disciplina = models.OneToOneField(Disciplina, on_delete = models.CASCADE, related_name = 'projeto_disciplina', null = True)
    linguagens = models.ManyToManyField(Linguagem, related_name = 'projetos_linguagem')

    def __str__(self):
            return self.nome_do_projeto