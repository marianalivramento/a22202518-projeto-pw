# Generated by Django 4.0.6 on 2024-05-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0018_alter_projeto_imagem_alter_projeto_link_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='apresentacao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='curso_fotos'),
        ),
    ]