from utils.db import db


class Parametros(db.Model):
    __tablename__ = 'parametros'
    idPar = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30),unique=True, nullable=False)
    estado = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP)
    detalles_parametros = db.relationship('Detalles_parametros', backref='parametros', lazy=True)

    def __init__(self,  nombre):
        self.nombre = nombre
        self.estado = 1

    def getDatos(self):
        return {
            'idPar': self.idPar,
            'nombre': self.nombre,
            'estado': self.estado,
            'created_at': self.created_at
        }