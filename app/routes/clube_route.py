import os.path
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename

from app import db
from app.models.mod_clube import Clube

clubeBluePrint = Blueprint('clubes', __name__)


@clubeBluePrint.route('/clubes')
def listar_clubes():
    clubes = Clube.query.order_by(Clube.nome).all()
    return render_template('clubes/index.html', clubes=clubes)


@clubeBluePrint.route('/cadastros/clube', methods=["GET", "POST"])
def cadastro_clubes():
    if request.method == "POST":
        nome = request.form['nome']
        fundacao = datetime.strptime(request.form['fundacao'], '%Y-%m-%d')
        estadio = request.form['estadio']
        cidade = request.form['cidade']
        pais = request.form['pais']
        escudo = request.files['escudo']
        escudo_file = None
        if escudo and escudo.filename != '':
            filename = secure_filename(escudo.filename)
            folder_path = os.path.join(current_app.root_path, 'static/img')
            os.makedirs(folder_path, exist_ok=True)
            escudo.save(os.path.join(folder_path, filename))
            escudo_file = f'img/{filename}'

        vitorias = request.form['vitorias']
        empates = request.form['empates']
        derrotas = request.form['derrotas']
        gols_pro = request.form['gols_pro']
        gols_contra = request.form['gols_contra']

        clube = Clube(
            nome=nome, fundacao=fundacao, estadio=estadio, cidade=cidade, pais=pais,
            vitorias=vitorias, empates=empates, derrotas=derrotas, gols_pro=gols_pro,
            gols_contra=gols_contra, escudo=escudo_file
        )
        db.session.add(clube)
        db.session.commit()

        return redirect(url_for('clubes.listar_clubes'))

    return render_template('cadastros/cad_clube.html')
