from flask import Flask, jsonify, request, Blueprint
from models.Usuario import *
from controllers import UsuarioController

users = Blueprint('users', __name__)



@users.route('/usuarios', methods=['GET','POST'])
def usuarios():
    return UsuarioController.usuarios()

@users.route('/usuarios/<idUsuario>')
def usuario(idUsuario):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    return UsuarioController.usuario(idUsuario)

@users.route('/usuarios/editar/<idUsuario>', methods=['PUT'])
def editarUsuario(idUsuario):
    return UsuarioController.editarUsuario(idUsuario)

@users.route('/usuarios/eliminar/<idUsuario>', methods=['DELETE'])
def eliminarUsuario(idUsuario):
    return UsuarioController.eliminarUsuario(idUsuario)
    