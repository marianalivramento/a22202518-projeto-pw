# Generated by Django 4.0.6 on 2024-03-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='ano_de_criacao',
            field=models.IntegerField(null=True, verbose_name='Ano de Criação'),
        ),
    ]