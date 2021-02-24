from app import db


class Doenca(db.Model):
    __tablename__ = 'doenca'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    sintomas = db.Column(db.Text)

    def __init__(self, nome, sintomas):
        self.nome = nome
        self.sintomas = sintomas
    
    def __repr__(self):
        return "<Doença %r>" % self.nome

class DadoEpidemiologico(db.Model):
    __tablename__ = 'dado_epidemiologico'

    id = db.Column(db.Integer, primary_key=True)
    data_coleta = db.Column(db.DateTime, nullable=False)
    doenca_associada_id = db.Column(db.Integer, db.ForeignKey('doenca.id'), nullable=True)
 
    doenca_associada = db.relationship('Doenca', foreign_keys=doenca_associada_id)

    def __init__(self, data_coleta, doenca_associada_id):
        self.data_coleta = data_coleta
        self.doenca_associada_id = doenca_associada_id

    def __repr__(self):
        return "<DadoEpidemiologico %r>" % self.data_coleta
