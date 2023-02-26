from flask import jsonify, request
from models.Vehiculo import *

def vehiculos():
    if request.method == 'GET':
        vehiculos = Vehiculos.query.all()
        if not vehiculos:
            return jsonify({'message': 'no hay vehiculos'})
        else:
            toVehiculos = [vehiculo.getDatos() for vehiculo in vehiculos]
            return jsonify(toVehiculos)
    elif request.method == 'POST':
        idUsuarioVeh = request.json["idUsuarioVeh"]
        placa = request.json["placa"]
        tipoV = request.json["tipoV"]
        new_vehiculo = Vehiculos(idUsuarioVeh, placa, tipoV)
        db.session.add(new_vehiculo)
        db.session.commit()
        return jsonify({'message':'vehiculo guardado con exito'})

def vehiculosActivos(estado):
    if request.method == 'GET':
        vehiculos = Vehiculos.query.filter_by(estado=estado).all()
        if not vehiculos:
            return jsonify({'message': 'no hay vehiculos activos'})
        else:
            toVehiculos = [vehiculo.getDatos() for vehiculo in vehiculos]
            return jsonify(toVehiculos)

def vehiculo(idVehiculo):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    vehiculo = Vehiculos.query.get(idVehiculo)
    if not vehiculo:
        return jsonify({'message': 'Vehiculo no encontrado'})
    else:
        return jsonify(vehiculo.getDatos())

def editarVehiculo(idVehiculo):
    vehiculo = Vehiculos.query.get(idVehiculo)
    if not vehiculo:
        return jsonify({'message': 'vehiculo no encontrado'})
    else:
        vehiculo.idUsuarioVeh = request.json["idUsuarioVeh"]
        vehiculo.placa = request.json["placa"]
        vehiculo.tipoV = request.json["tipoV"]
        db.session.commit()
        return jsonify({'message': 'Vehiculo actualizado con exito'})

def eliminarVehiculo(idVehiculo):
    Vehiculo = Vehiculos.query.get(idVehiculo)
    if not Vehiculo:
        return jsonify({'message': 'Vehiculo no encontrado'})
    else:
        db.session.delete(Vehiculo)
        db.session.commit()
        return jsonify({'message': 'Vehiculo eliminado con exito'})