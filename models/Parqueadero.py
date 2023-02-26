from utils.db import db


class Parqueaderos(db.Model):
    __tablename__ = 'parqueaderos'
    idParquedero = db.Column(db.Integer, primary_key=True)
    idUsuarioPar = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuario'), nullable=False)
    direccion = db.Column(db.String(50),unique=True, nullable=False)
    longitud = db.Column(db.String(100),nullable=False)
    latitud = db.Column(db.String(100),nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    horaApertura = db.Column(db.TIME, nullable=False)
    horaCierre = db.Column(db.TIME, nullable=False)
    puestos = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.TIMESTAMP)

    def __init__(self,  idUsuarioPar, direccion,longitud,latitud, precio, horaApertura, horaCierre,puestos):
        self.idUsuarioPar = idUsuarioPar
        self.direccion = direccion
        self.longitud = longitud
        self.latitud = latitud
        self.precio = precio
        self.horaApertura = horaApertura
        self.horaCierre = horaCierre
        self.puestos = puestos
        self.estado = 1

    def getDatos(self):
        return {
            'idParquedero': self.idParquedero,
            'idUsuarioPar': self.idUsuarioPar,
            'direccion': self.direccion,
            'longitud' : float(self.longitud),
            'latitud' : float(self.latitud),
            'precio': self.precio,
            'horaApertura': str(self.horaApertura),
            'horaCierre': str(self.horaCierre),
            'puestos':self.puestos,
            'estado': self.estado,
            'created_at': self.created_at
        }