# Generated by Django 4.0.6 on 2024-03-29 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('resumo', models.TextField(blank=True)),
                ('link', models.URLField()),
                ('data_de_publicacao', models.IntegerField(verbose_name='Data de Publicação')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano_de_inscricao', models.IntegerField(verbose_name='Ano de Inscrição')),
                ('foto_de_perfil', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='artigos.artigo')),
                ('autor_do_rating', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='artigos.utilizador')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='artigos.artigo')),
                ('autor_do_comentario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='artigos.utilizador')),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='autor',
            field=models.ManyToManyField(related_name='artigo', to='artigos.autor'),
        ),
    ]
