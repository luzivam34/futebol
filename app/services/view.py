from collections import OrderedDict

from django.shortcuts import render

from app.models.mod_partida import Partida


def sua_view(request):
    partidas = Partida.objects.all()

    campeonatos_unicos = OrderedDict()
    for partida in partidas:
        if partida.campeonato not in campeonatos_unicos:
            campeonatos_unicos[partida.campeonato] = partida

    context = {
        'partidas': campeonatos_unicos.values()
    }
    return render(request, 'cad_partidas.html', context)
