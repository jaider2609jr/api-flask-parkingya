from flask import jsonify, request
from models.Usuario import *


def usuarios():
    if request.method == 'GET':
        usuarios = Usuarios.query.all()
        if not usuarios:
            return jsonify({'message': 'no hay usuarios'})
        else:
            toUsers = [usuario.getDatos() for usuario in usuarios]
            return jsonify(toUsers)
    elif request.method == 'POST':
        username = request.json["username"]
        password = request.json["password"]
        correo = request.json["correo"]
        pNombre = request.json["pNombre"]
        sNombre = request.json["sNombre"]
        pApellido = request.json["pApellido"]
        sApellido = request.json["sApellido"]
        tipoId = int(request.json["tipoId"])
        numeroId = request.json["numeroId"]
        new_usuario = Usuarios(username,password,correo,pNombre,sNombre,pApellido,sApellido,tipoId,numeroId)
        db.session.add(new_usuario)
        db.session.commit()
        return jsonify({
            'message':'Usuario registrado con exito',
            'status':'ok'
            })

def usuario(idUsuario):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    usuario = Usuarios.query.get(idUsuario)
    if not usuario:
        return jsonify({'message': 'Usuario not found'})
    else:
        return jsonify(usuario.getDatos())

def editarUsuario(idUsuario):
    usuario = Usuarios.query.get(idUsuario)
    if not usuario:
        return jsonify({'message': 'Usuario not found'})
    else:
        usuario.username = request.json["username"]
        usuario.password = request.json["password"]
        usuario.correo = request.json["correo"]
        usuario.pNombre = request.json["pNombre"]
        usuario.sNombre = request.json["sNombre"]
        usuario.pApellido = request.json["pApellido"]
        usuario.sApellido = request.json["sApellido"]
        usuario.tipoId = int(request.json["tipoId"])
        usuario.numeroId = request.json["numeroId"]
        db.session.commit()
        return jsonify({'message': 'Datos actualizados con exito'})

def eliminarUsuario(idUsuario):
    usuario = Usuarios.query.get(idUsuario)
    if not usuario:
        return jsonify({'message': 'Usuario not found'})
    else:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado con exito'})