from flask import Blueprint, render_template

mainBluePrint = Blueprint('main', __name__)


@mainBluePrint.route('/')
def index():
    return render_template('index.html')


@mainBluePrint.route('/cadastros')
def cadastros():
    return render_template('cadastros/index.html')


@mainBluePrint.route('/clubes')
def clubes():
    return render_template('clubes/index.html')


@mainBluePrint.route('/campeonatos')
def campeonatos():
    return render_template('campeonatos/index.html')


@mainBluePrint.route('/gamer')
def gamer():
    return render_template('gamer/index.html')
