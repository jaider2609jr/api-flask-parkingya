from flask import Flask, jsonify, request, Blueprint
from models.Detalles_parametros import *
from controllers import DetallerParamController

deparametros = Blueprint('deparametros', __name__)

@deparametros.route('/dparametros', methods=['GET','POST'])
def dparametros():
    return DetallerParamController.dparametros()

@deparametros.route('/dparametros/<idDet>')
def dparametro(idDet):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    return DetallerParamController.dparametro(idDet)

@deparametros.route('/dparametros/editar/<idDet>', methods=['PUT'])
def editarDP(idDet):
    return DetallerParamController.editarDP(idDet)

@deparametros.route('/dparametros/eliminar/<idDet>', methods=['DELETE'])
def eliminarDP(idDet):
    return DetallerParamController.eliminarDP(idDet)