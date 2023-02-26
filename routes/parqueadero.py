from flask import Flask, jsonify, request, Blueprint
from models.Parqueadero import *
from controllers import ParqueaderoController

parking = Blueprint('parking', __name__)

@parking.route('/parqueaderos', methods=['GET','POST'])
def parqueaderos():
    return ParqueaderoController.parqueaderos()

@parking.route('/parqueaderos/activos/<idUsuarioPar>')
def parqueaderosUsuarioA(idUsuarioPar):
    return ParqueaderoController.parqueaderosUsuarioA(idUsuarioPar)

@parking.route('/parqueaderos/inactivos/<idUsuarioPar>')
def parqueaderosUsuarioI(idUsuarioPar):
    return ParqueaderoController.parqueaderosUsuarioI(idUsuarioPar)


@parking.route('/parqueaderos/<idParquedero>')
def parqueadero(idParquedero):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    return ParqueaderoController.parqueadero(idParquedero)

@parking.route('/parqueaderos/editar/<idParquedero>', methods=['PUT'])
def editarParqueadero(idParquedero):
    return ParqueaderoController.editarParqueadero(idParquedero)

@parking.route('/parqueaderos/eliminar/<idParquedero>', methods=['PUT'])
def eliminarParqueadero(idParquedero):
    return ParqueaderoController.eliminarParqueadero(idParquedero)

@parking.route('/parqueaderos/recuperar/<idParquedero>', methods=['PUT'])
def recuperarParqueadero(idParquedero):
    return ParqueaderoController.recuperarParqueadero(idParquedero)

