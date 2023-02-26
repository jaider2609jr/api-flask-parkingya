from flask import Flask, jsonify, request, Blueprint
from models.Parametros import *
from controllers import ParametrosController

parame = Blueprint('parame', __name__)

@parame.route('/parametros', methods=['GET','POST'])
def parametros():
    return ParametrosController.parametros()

@parame.route('/parametros/<idPar>')
def parametro(idPar):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    return ParametrosController.parametro(idPar)

@parame.route('/parametros/editar/<idPar>', methods=['PUT'])
def editarParametro(idPar):
    return ParametrosController.editarParametro(idPar)

@parame.route('/parametros/eliminar/<idPar>', methods=['DELETE'])
def eliminarParametro(idPar):
    return ParametrosController.eliminarParametro(idPar)