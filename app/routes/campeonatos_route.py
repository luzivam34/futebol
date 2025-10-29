from flask import Blueprint, render_template
from sqlalchemy import or_

from app.models.mod_clube import Clube
from app.models.mod_partida import Partida
from app.services.estatiticas_service import atualizar_resultados, atualizar_gols

campBlueprint = Blueprint('campbp', __name__)


@campBlueprint.route('/rank')
def rank():
    clubes = Clube.query.all()
    partidas = Partida.query.all()
    atualizar_gols(partidas)
    atualizar_resultados(partidas)
    return render_template('campeonatos/rank.html', partidas=partidas, clubes=clubes)


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

    return render_template('/campeonatos/paulistao.html', partidas=partidas, paulista=paulista)


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
