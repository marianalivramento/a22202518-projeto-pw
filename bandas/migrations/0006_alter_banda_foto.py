# Generated by Django 4.0.6 on 2024-04-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0005_alter_album_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='banda/fotos'),
        ),
    ]