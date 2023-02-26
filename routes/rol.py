from flask import Flask, jsonify, request, Blueprint
from models.Rol import *
from controllers import RolesController

roluser = Blueprint('roluser', __name__)

@roluser.route('/roles', methods=['GET','POST'])
def roles():
    return RolesController.roles()

@roluser.route('/roles/<id>')
def rol(id):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    return RolesController.rol(id)

@roluser.route('/roles/editar/<id>', methods=['PUT'])
def editarRol(id):
    return RolesController.editarRol(id)

@roluser.route('/roles/eliminar/<id>', methods=['DELETE'])
def eliminarRol(id):
    return RolesController.eliminarRol(id)