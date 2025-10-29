from flask import Blueprint, render_template, request, redirect, url_for

from app.models.mod_gamer import JogadorGamer

gamerBluePrint = Blueprint('gamerbp', __name__)


@gamerBluePrint.route('/gamerjogador')
def gamer_jogador():
    jogadores = JogadorGamer.query.all()
    return render_template('gamer/jogador.html', jogadores=jogadores)


@gamerBluePrint.route('/alistarjogador', methods=['POST', 'GET'])
def alistar():
    if request.method == "POST":
        return redirect(url_for('gamerbp.gamer_jogador'))
    return render_template('gamer/alistar.html')
