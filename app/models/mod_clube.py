from sqlalchemy import or_

from app import db
from app.models.mod_partida import Partida


class Clube(db.Model):
    __tablename__ = 'clube'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    fundacao = db.Column(db.Date, nullable=False)
    estadio = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(100), nullable=False)
    escudo = db.Column(db.String(200))
    vitorias = db.Column(db.Integer, nullable=False, default=0)
    empates = db.Column(db.Integer, nullable=False, default=0)
    derrotas = db.Column(db.Integer, nullable=False, default=0)
    gols_pro = db.Column(db.Integer, nullable=False, default=0)
    gols_contra = db.Column(db.Integer, nullable=False, default=0)
    estadual = db.Column(db.Integer, default=0)
    divisao = db.Column(db.String(100))

    partidas_mandante = db.relationship(
        'Partida', foreign_keys='Partida.mandante_id',
        backref='mandante_clube',
        lazy=True
    )
    partidas_visitante = db.relationship(
        'Partida',
        foreign_keys='Partida.visitante_id',
        backref='visitante_clube',
        lazy=True
    )

    def partidas_por_campeonato(self, campeonato):
        return Partida.query.filter(
            or_(
                Partida.mandante_id == self.id,
                Partida.visitante_id == self.id
            ),
            Partida.campeonato == campeonato
        ).all()
