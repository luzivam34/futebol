from flask import Blueprint, render_template

from app.models.mod_clube import Clube
from app.models.mod_partida import Partida
from app.services.estatiticas_service import atualizar_gols, atualizar_resultados

mainBluePrint = Blueprint('main', __name__)


@mainBluePrint.route('/')
def index():
    return render_template('index.html')


@mainBluePrint.route('/cadastros')
def cadastros():
    return render_template('cadastros/index.html')


@mainBluePrint.route('/rank')
def rank():
    clubes = Clube.query.all()
    partidas = Partida.query.all()
    atualizar_gols()
    atualizar_resultados()
    return render_template('rank.html', partidas=partidas, clubes=clubes)


@mainBluePrint.route('/gamer')
def gamer():
    return render_template('gamer/index.html')
