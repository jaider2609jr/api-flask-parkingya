from flask import jsonify, request
from models.Detalles_parametros import *

def dparametros():
    if request.method == 'GET':
        detalles = Detalles_parametros.query.all()
        if not detalles:
            return jsonify({'message': 'no hay detalles parametros'})
        else:
            toDetalles = [detalle.getDatos() for detalle in detalles]
            return jsonify(toDetalles)
    elif request.method == 'POST':
        idDetPar = request.json["idDetPar"]
        nombre = request.json["nombre"]
        new_detalles = Detalles_parametros(idDetPar, nombre)
        db.session.add(new_detalles)
        db.session.commit()
        return jsonify({'message':'detalle de parametro guardado con exito'})

def dparametro(idDetPar):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    #detalle = Detalles_parametros.query.get(idDet)
    detalles = Detalles_parametros.query.filter_by(idDetPar=idDetPar).all()
    if not detalles:
        return jsonify({'message': 'detalles parametros no encontrados'})
    else:
        toDetalles = [detalle.getDatos() for detalle in detalles]
        return jsonify(toDetalles)

def editarDP(idDet):
    detalle = Detalles_parametros.query.get(idDet)
    if not detalle:
        return jsonify({'message': 'detalle parametro no encontrado'})
    else:
        detalle.idDetPar = request.json["idDetPar"]
        detalle.nombre = request.json["nombre"]
        db.session.commit()
        return jsonify({'message': 'detalle de parametro actualizado con exito'})

def eliminarDP(idDet):
    detalle = Detalles_parametros.query.get(idDet)
    if not detalle:
        return jsonify({'message': 'detalle parametro no encontrado'})
    else:
        db.session.delete(detalle)
        db.session.commit()
        return jsonify({'message': 'detalle de parametro eliminado con exito'})