from flask import Blueprint, render_template
from sqlalchemy import or_

from app.models.mod_clube import Clube
from app.models.mod_partida import Partida
from app.services.estatiticas_service import atualizar_resultados, atualizar_gols, buscar_clubes_por_nome

campBlueprint = Blueprint('campbp', __name__)


@campBlueprint.route('/rank')
def rank():
    clubes = Clube.query.all()
    partidas = Partida.query.all()
    atualizar_gols(partidas)
    atualizar_resultados(partidas)
    return render_template('campeonatos/rank.html', partidas=partidas, clubes=clubes)


@campBlueprint.route('/libertadores')
def libertadores():
    partidas = Partida.query.filter_by(campeonato='Libertadores').all()

    atualizar_gols(partidas)
    atualizar_resultados(partidas)

    libertadores = (
        Clube.query
        .join(Partida, or_(
            Clube.id == Partida.mandante_id,
            Clube.id == Partida.visitante_id
        ))
        .filter(Partida.campeonato == 'Libertadores')
        .distinct()
        .all()
    )

    return render_template('/campeonatos/libertadores.html', partidas=partidas, libertadores=libertadores)


@campBlueprint.route('/brasil')
def brasil():
    return render_template('campeonatos/brasil/index.html')


@campBlueprint.route('/paulistao')
def paulistao():
    partidas = Partida.query.filter_by(campeonato='Paulistao_A1').all()

    atualizar_gols(partidas)
    atualizar_resultados(partidas)

    paulista = (
        Clube.query
        .join(Partida, or_(
            Clube.id == Partida.mandante_id,
            Clube.id == Partida.visitante_id
        ))
        .filter(Partida.campeonato == 'Paulistao_A1')
        .distinct()
        .all()
    )

    grupoA = buscar_clubes_por_nome(['Corinthians', 'Mirassol', 'Inter de Limeira', 'Botafogo FC'])
    grupoB = buscar_clubes_por_nome(['Santos FC', 'Guarani', 'Portuguesa', 'Red Bull Bragantino'])
    grupoC = buscar_clubes_por_nome(['São Paulo', 'Grêmio Novorizontino', 'Noroeste', 'Água Santa'])
    grupoD = buscar_clubes_por_nome(['Ponte Preta', 'São Bernardo', 'Palmeiras', 'Velo Clube'])

    quartasfinais = Partida.query.order_by(Partida.data).filter_by(campeonato='Paulistao A1 Quartas finais').all()
    semifinais = Partida.query.order_by(Partida.data).filter_by(campeonato='Paulistao A1 Semi Finais').all()
    finais = Partida.query.order_by(Partida.data).filter_by(campeonato='Paulistao A1 Finais').all()

    return render_template('/campeonatos/paulistao.html',
                           partidas=partidas,
                           paulista=paulista,
                           grupoA=grupoA,
                           grupoB=grupoB,
                           grupoC=grupoC,
                           grupoD=grupoD,
                           quartasfinais=quartasfinais,
                           semifinais=semifinais,
                           finais=finais
                           )


@campBlueprint.route('/carioca')
def carioca():
    return render_template('campeonatos/brasil/carioca/index.html')
