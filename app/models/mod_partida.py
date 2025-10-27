from app import db


class Partida(db.Model):
    __tablename__ = 'partida'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    estadio = db.Column(db.String(150))
    campeonato = db.Column(db.String(150))
    mandante_id = db.Column(db.Integer, db.ForeignKey('clube.id'))
    visitante_id = db.Column(db.Integer, db.ForeignKey('clube.id'))
    gols_mandante = db.Column(db.Integer, default=0)
    gols_visitante = db.Column(db.Integer, default=0)

    mandante = db.relationship("Clube", foreign_keys=[mandante_id])
    visitante = db.relationship("Clube", foreign_keys=[visitante_id])
