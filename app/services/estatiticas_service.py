from sqlalchemy import or_

from app import db
from app.models.mod_clube import Clube
from app.models.mod_partida import Partida


def atualizar_gols(partidas):
    clubes_ids = set()
    for partida in partidas:
        clubes_ids.add(partida.mandante_id)
        clubes_ids.add(partida.visitante_id)

    clubes = Clube.query.filter(Clube.id.in_(clubes_ids)).all()
    for clube in clubes:
        clube.gols_pro = 0
        clube.gols_contra = 0

    for partida in partidas:
        mandante = Clube.query.get(partida.mandante_id)
        visitante = Clube.query.get(partida.visitante_id)

        if mandante:
            mandante.gols_pro += partida.gols_mandante
            mandante.gols_contra += partida.gols_visitante

        if visitante:
            visitante.gols_pro += partida.gols_visitante
            visitante.gols_contra += partida.gols_mandante

    db.session.commit()


def atualizar_resultados(partidas):
    clubes_ids = set()
    for partida in partidas:
        clubes_ids.add(partida.mandante_id)
        clubes_ids.add(partida.visitante_id)

    clubes = Clube.query.filter(Clube.id.in_(clubes_ids)).all()

    # Zera os dados antes de recalcular
    for clube in clubes:
        clube.vitorias = 0
        clube.empates = 0
        clube.derrotas = 0

    for partida in partidas:
        mandante = Clube.query.get(partida.mandante_id)
        visitante = Clube.query.get(partida.visitante_id)

        if partida.gols_mandante > partida.gols_visitante:
            if mandante:
                mandante.vitorias += 1
            if visitante:
                visitante.derrotas += 1

        elif partida.gols_mandante < partida.gols_visitante:
            if visitante:
                visitante.vitorias += 1
            if mandante:
                mandante.derrotas += 1

        else:  # empate
            if mandante:
                mandante.empates += 1
            if visitante:
                visitante.empates += 1

    db.session.commit()


def buscar_clubes_por_nome(nomes):
    return (
        Clube.query
        .join(Partida, or_(Clube.id == Partida.mandante_id, Clube.id == Partida.visitante_id
                           ))
        .filter(Clube.nome.in_(nomes))
        .distinct()
        .all()
    )


def buscar_partidas_por_campeonato(campeonato):
    return (
        Clube.query
        .join(Partida, or_(Clube.id == Partida.mandante_id, Clube.id == Partida.visitante_id))
        .filter(Partida.campeonato.in_(campeonato))
        .distinct()
        .all()
    )
