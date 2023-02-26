from utils.db import db


class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20),unique=True, nullable=False)
    usuarios = db.relationship('Usuarios', backref='roles', lazy=True)

    def __init__(self,  nombre):
        self.nombre = nombre

    def getDatos(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }