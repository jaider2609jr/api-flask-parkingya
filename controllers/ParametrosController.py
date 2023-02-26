from flask import jsonify, request
from models.Parametros import *

def parametros():
    if request.method == 'GET':
        parametros = Parametros.query.all()
        if not parametros:
            return jsonify({'message': 'no hay parametros'})
        else:
            toParametros = [parametro.getDatos() for parametro in parametros]
            return jsonify(toParametros)
    elif request.method == 'POST':
        nombre = request.json["nombre"]
        new_parametro = Parametros(nombre)
        db.session.add(new_parametro)
        db.session.commit()
        return jsonify({'message':'parametro guardado con exito'})

def parametro(idPar):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    parametro = Parametros.query.get(idPar)
    if not parametro:
        return jsonify({'message': 'parametro no encontrado'})
    else:
        return jsonify(parametro.getDatos())

def editarParametro(idPar):
    parametro = Parametros.query.get(idPar)
    if not parametro:
        return jsonify({'message': 'parametro no encontrado'})
    else:
        parametro.nombre = request.json["nombre"]
        db.session.commit()
        return jsonify({'message': 'parametro actualizado con exito'})

def eliminarParametro(idPar):
    parametro = Parametros.query.get(idPar)
    if not parametro:
        return jsonify({'message': 'parametro no encontrado'})
    else:
        db.session.delete(parametro)
        db.session.commit()
        return jsonify({'message': 'parametro eliminado con exito'})