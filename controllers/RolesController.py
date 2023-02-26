from flask import jsonify, request
from models.Rol import *

def roles():
    if request.method == 'GET':
        rolesU = Roles.query.all()
        if not rolesU:
            return jsonify({'message': 'no hay roles'})
        else:
            toRoles = [rol.getDatos() for rol in rolesU]
            return jsonify(toRoles)
    elif request.method == 'POST':
        nombre = request.json["nombre"]
        new_rol = Roles(nombre)
        db.session.add(new_rol)
        db.session.commit()
        return jsonify({'message':'rol guardado con exito'})

def rol(id):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    rol = Roles.query.get(id)
    if not rol:
        return jsonify({'message': 'rol no encontrado'})
    else:
        return jsonify(rol.getDatos())

def editarRol(id):
    rol = Roles.query.get(id)
    if not rol:
        return jsonify({'message': 'rol no encontrado'})
    else:
        rol.nombre = request.json["nombre"]
        db.session.commit()
        return jsonify({'message': 'rol actualizado con exito'})

def eliminarRol(id):
    rol = Roles.query.get(id)
    if not rol:
        return jsonify({'message': 'rol no encontrado'})
    else:
        db.session.delete(rol)
        db.session.commit()
        return jsonify({'message': 'rol eliminado con exito'})