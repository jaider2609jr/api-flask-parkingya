from enum import unique
from utils.db import db


class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    pNombre = db.Column(db.String(15), nullable=False)
    sNombre = db.Column(db.String(15), nullable=True)
    pApellido = db.Column(db.String(15), nullable=False)
    sApellido = db.Column(db.String(15), nullable=False)
    tipoId = db.Column(db.Integer, db.ForeignKey('detalles_parametros.idDet'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    numeroId = db.Column(db.Integer, unique=True, nullable=False)
    estado = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP)
    vehiculos = db.relationship('Vehiculos', backref='usuarios', lazy=True)
    parqueaderos = db.relationship('Parqueaderos', backref='usuarios', lazy=True)

    def __init__(self, username, password, correo, pNombre, sNombre, pApellido, sApellido, tipoId, numeroId):
        self.username = username
        self.password = password
        self.correo = correo
        self.pNombre = pNombre
        self.sNombre = sNombre
        self.pApellido = pApellido
        self.sApellido = sApellido
        self.numeroId = numeroId
        self.tipoId = tipoId
        self.rol_id = 2
        self.estado = 1

    def getDatos(self):
        return {
            'idUsuario': self.idUsuario,
            'username': self.username,
            'password': self.password,
            'correo': self.correo,
            'pNombre': self.pNombre,
            'sNombre': self.sNombre,
            'pApellido': self.pApellido,
            'sApellido': self.sApellido,
            'tipoId': self.tipoId,
            'rol_id': self.rol_id,
            'numeroId': self.numeroId,
            'estado': self.estado,
            'created_at': self.created_at
        }