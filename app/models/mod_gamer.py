from app import db


class JogadorGamer(db.Model):
    __tablename__ = 'JogadorGamer'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    nation = db.Column(db.String(100))
    overal = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(100))
    altura = db.Column(db.Float)
    peso = db.Column(db.Float)
