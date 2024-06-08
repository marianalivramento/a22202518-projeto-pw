from bandas.models import Banda
from bandas.models import Album
from bandas.models import Musica
import json

Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()


with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)

    for banda in bandas:

        Banda.objects.create(
                nome_banda = banda['nome_banda'],
                nacionalidade = banda['nacionalidade'],
                ano_de_criacao = banda['ano_de_criacao'],
            )

with open('bandas/json/albuns.json') as f:
    albuns = json.load(f)

    for banda_data in albuns:
        banda_nome = banda_data['banda']

        try:
            banda_item = Banda.objects.get(nome_banda=banda_nome)
        except Banda.DoesNotExist:
            banda_item = Banda.objects.create(nome_banda = banda_nome)


        for album in banda_data['albums']:
            new_album = Album.objects.create(
                nome_album = album['nome_album'],
                ano_de_lancamento = album['ano_de_lancamento'],
                banda = banda_item
            )

            for musica in album['musicas']:
                Musica.objects.create(
                    nome_musica = musica['nome_musica'],
                    duracao = musica['duracao'],
                    data_lancamento = musica['ano_de_lancamento'],
                    banda = banda_item
                )

                new_album.musica.add(Musica.objects.get(nome_musica=musica['nome_musica']))





