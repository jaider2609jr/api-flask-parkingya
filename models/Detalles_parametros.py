from utils.db import db

class Detalles_parametros(db.Model):
    __tablename__ = 'detalles_parametros'
    idDet = db.Column(db.Integer, primary_key=True)
    idDetPar = db.Column(db.Integer, db.ForeignKey('parametros.idPar'), nullable=False)
    nombre = db.Column(db.String(30),unique=True, nullable=False)
    estado = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP)
    usuarios = db.relationship('Usuarios', backref='detalles_parametros', lazy=True)

    def __init__(self, idDetPar, nombre):
        self.idDetPar = idDetPar
        self.nombre = nombre
        self.estado = 1

    def getDatos(self):
        return {
            'idDet': self.idDet,
            'idDetPar': self.idDetPar,
            'nombre': self.nombre,
            'estado': self.estado,
            'created_at': self.created_at
        }