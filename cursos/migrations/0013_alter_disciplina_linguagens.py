# Generated by Django 4.0.6 on 2024-04-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0012_alter_disciplina_linguagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='linguagens',
            field=models.ManyToManyField(blank=True, related_name='disciplina', to='cursos.linguagem'),
        ),
    ]