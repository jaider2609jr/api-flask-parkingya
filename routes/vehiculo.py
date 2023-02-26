from flask import Flask, jsonify, request, Blueprint
from models.Vehiculo import *
from controllers import VehiculoController

vehicle = Blueprint('vehicle', __name__)

@vehicle.route('/vehiculos', methods=['GET','POST'])
def vehiculos():
    return VehiculoController.vehiculos()

@vehicle.route('/vehiculos/<idVehiculo>')
def vehiculo(idVehiculo):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    return VehiculoController.vehiculo(idVehiculo)

@vehicle.route('/vehiculos/activos/<estado>')
def vehiculosActivos(estado):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    return VehiculoController.vehiculosActivos(estado)

@vehicle.route('/vehiculos/editar/<idVehiculo>', methods=['PUT'])
def editarVehiculo(idVehiculo):
    return VehiculoController.editarVehiculo(idVehiculo)

@vehicle.route('/vehiculos/eliminar/<idVehiculo>', methods=['DELETE'])
def eliminarVehiculo(idVehiculo):
    return VehiculoController.eliminarVehiculo(idVehiculo)