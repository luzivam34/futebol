from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import desc

from app import db
from app.models.mod_clube import Clube
from app.models.mod_partida import Partida
from app.services.estatiticas_service import atualizar_gols, atualizar_resultados

partidaBluePrint = Blueprint('partida', __name__)


@partidaBluePrint.route('/partidas')
def lista_partida():
    partidas = Partida.query.order_by(desc(Partida.data)).all()
    return render_template('partidas/index.html', partidas=partidas)


@partidaBluePrint.route('/cadastros/partidas', methods=['POST', 'GET'])
def cadastrar_partida():
    clubes = Clube.query.all()
    partidas = Partida.query.all()
    if request.method == "POST":
        data = request.form['data']
        estadio = request.form['estadio']
        mandante_id = request.form['mandante_id']
        visitante_id = request.form['visitante_id']
        gols_mandante = int(request.form['gols_mandante'])
        gols_visitante = int(request.form['gols_visitante'])

        nova_partida = Partida(
            data=data,
            estadio=estadio,
            mandante_id=mandante_id,
            visitante_id=visitante_id,
            gols_mandante=gols_mandante,
            gols_visitante=gols_visitante
        )

        db.session.add(nova_partida)
        db.session.commit()

        # Atualiza estatísticas
        atualizar_gols()
        atualizar_resultados()

        return redirect(url_for('partida.lista_partida'))

    return render_template('cadastros/cad_partidas.html', clubes=clubes, partidas=partidas)
