from flask import Blueprint, render_template, request
from sqlalchemy import or_, desc
from sqlalchemy.orm import aliased

from app import db
from app.models.mod_clube import Clube
from app.models.mod_partida import Partida
from app.services.estatiticas_service import atualizar_gols, atualizar_resultados

estaduaisBlueprint = Blueprint('estadual', __name__)


@estaduaisBlueprint.route('/estaduais')
def estaduais():
    return render_template('campeonatos/brasil/estaduais/index.html')


@estaduaisBlueprint.route('/estaduais/saopaulo')
def estaduais_saopaulo():
    return render_template('campeonatos/brasil/estaduais/paulista/index.html')


@estaduaisBlueprint.route('/paulista2025')
def paulista2025():
    return render_template('campeonatos/brasil/estaduais/paulista/paulista2025/paulista2025.html')


@estaduaisBlueprint.route('/paulista2025/classificacaogeral', methods=['GET'])
def classificacao_geral_paulista2025():
    busca = request.args.get('busca', '')

    mandante_alias = aliased(Clube)
    visitante_alias = aliased(Clube)

    partidas_completas = (
        db.session.query(Partida)
        .filter(Partida.campeonato == 'Paulistao A1 - 2025')
        .order_by(desc(Partida.data))
        .all()
    )

    partidas_query = (
        db.session.query(Partida, mandante_alias.nome.label('mandante_nome'),
                         visitante_alias.nome.label('visitante_nome'))
        .join(mandante_alias, Partida.mandante_id == mandante_alias.id)
        .join(visitante_alias, Partida.visitante_id == visitante_alias.id)
        .filter(Partida.campeonato == 'Paulistao A1 - 2025')
        .order_by(desc(Partida.data))
    )

    if busca:
        partidas_query = partidas_query.filter(
            db.or_(
                mandante_alias.nome.ilike(f'%{busca}%'),
                visitante_alias.nome.ilike(f'%{busca}%')
            )
        )

    partidas_filtradas = partidas_query.all()
    total = len(partidas_filtradas)

    atualizar_gols(partidas_completas)
    atualizar_resultados(partidas_completas)

    clubes_paulista_2025 = (
        Clube.query
        .join(Partida, or_(
            Clube.id == Partida.mandante_id,
            Clube.id == Partida.visitante_id
        ))
        .filter(Partida.campeonato == 'Paulistao A1 - 2025')
        .distinct()
        .all()
    )

    return render_template('campeonatos/brasil/estaduais/paulista/paulista2025/classificacao_geral.html',
                           partidas=partidas_filtradas,
                           busca=busca,
                           clubes=clubes_paulista_2025,
                           total=total
                           )
