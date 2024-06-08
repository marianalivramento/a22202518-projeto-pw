# Generated by Django 4.0.6 on 2024-04-23 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praias', '0002_praia_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regiao',
            name='praia',
        ),
        migrations.AddField(
            model_name='regiao',
            name='praia',
            field=models.ManyToManyField(related_name='regiao', to='praias.praia'),
        ),
    ]
