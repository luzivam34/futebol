from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import desc
from sqlalchemy.orm import aliased

from app import db
from app.models.mod_clube import Clube
from app.models.mod_partida import Partida
from app.services.estatiticas_service import atualizar_gols, atualizar_resultados

partidaBluePrint = Blueprint('partida', __name__)


@partidaBluePrint.route('/partidas')
def lista_partida():
    busca = request.args.get('busca', '')

    mandante_alias = aliased(Clube)
    visitante_alias = aliased(Clube)

    query = (
        db.session.query(Partida, mandante_alias.nome.label('mandante_nome'),
                         visitante_alias.nome.label('visitante_nome'))
        .join(mandante_alias, Partida.mandante_id == mandante_alias.id)
        .join(visitante_alias, Partida.visitante_id == visitante_alias.id)
    )

    if busca:
        query = query.filter(
            db.or_(
                mandante_alias.nome.ilike(f'%{busca}%'),
                visitante_alias.nome.ilike(f'%{busca}%')
            )
        )

    partidas = query.order_by(desc(Partida.data)).all()

    total = len(partidas)

    return render_template('partidas/index.html', partidas=partidas, busca=busca, total=total)


@partidaBluePrint.route('/cadastros/partidas', methods=['POST', 'GET'])
def cadastrar_partida():
    clubes = Clube.query.order_by(Clube.nome).all()
    
    from collections import OrderedDict

    partidas_raw = Partida.query.all()
    campeonatos_unicos = OrderedDict()
    for partida in partidas_raw:
        if partida.campeonato not in campeonatos_unicos:
            campeonatos_unicos[partida.campeonato] = partida

    partidas = campeonatos_unicos.values()

    if request.method == "POST":
        data = request.form['data']
        estadio = request.form['estadio']
        mandante_id = request.form['mandante_id']
        visitante_id = request.form['visitante_id']
        gols_mandante = int(request.form['gols_mandante'])
        gols_visitante = int(request.form['gols_visitante'])
        campeonato = request.form['campeonato']

        nova_partida = Partida(
            data=data,
            estadio=estadio,
            mandante_id=mandante_id,
            visitante_id=visitante_id,
            gols_mandante=gols_mandante,
            gols_visitante=gols_visitante,
            campeonato=campeonato

        )

        db.session.add(nova_partida)
        db.session.commit()

        # Atualiza estatísticas
        atualizar_gols(partidas)
        atualizar_resultados(partidas)

        return redirect(url_for('partida.lista_partida'))

    return render_template('cadastros/cad_partidas.html', clubes=clubes, partidas=partidas)
