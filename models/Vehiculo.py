from utils.db import db


class Vehiculos(db.Model):
    __tablename__ = 'vehiculos'
    idVehiculo = db.Column(db.Integer, primary_key=True)
    idUsuarioVeh = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuario'), nullable=False)
    placa = db.Column(db.String(10),unique=True, nullable=False)
    tipoV = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP)

    def __init__(self,  idUsuarioVeh, placa, tipoV):
        self.idUsuarioVeh = idUsuarioVeh
        self.placa = placa
        self.tipoV = tipoV
        self.estado = 1

    def getDatos(self):
        return {
            'idVehiculo': self.idVehiculo,
            'idUsuarioVeh': self.idVehiculo,
            'placa': self.placa,
            'tipoV': self.tipoV,
            'estado': self.estado,
            'created_at': self.created_at
        }