from flask import jsonify, request
from models.Parqueadero import *

def parqueaderos():
    if request.method == 'GET':
        parqueaderos = Parqueaderos.query.filter_by(estado=1).all()
        if not parqueaderos:
            return jsonify({'message': 'no hay parqueaderos'})
        else:
            toParqueaderos = [parqueadero.getDatos() for parqueadero in parqueaderos]
            return jsonify(toParqueaderos)
    elif request.method == 'POST':
        idUsuarioPar = request.json["idUsuarioPar"]
        direccion = request.json["direccion"]
        longitud = str(request.json["longitud"])
        latitud = str(request.json["latitud"])
        precio = request.json["precio"]
        horaApertura = request.json["horaApertura"]
        horaCierre = request.json["horaCierre"]
        puestos = request.json["puestos"]
        new_parqueadero = Parqueaderos(idUsuarioPar, direccion,longitud,latitud, precio, horaApertura, horaCierre,puestos)
        db.session.add(new_parqueadero)
        db.session.commit()
        return jsonify({'message':'parqueadero guardado con exito'})

def parqueaderosUsuarioA(idUsuarioPar):
    if request.method == 'GET':
        parqueaderos = Parqueaderos.query.filter_by(estado=1, idUsuarioPar=idUsuarioPar).all()
        if not parqueaderos:
            #return jsonify({'message': 'no hay parqueaderos activos'})
            return jsonify([])
        else:
            toParqueaderos = [parqueadero.getDatos() for parqueadero in parqueaderos]
            return jsonify(toParqueaderos) 


def parqueaderosUsuarioI(idUsuarioPar):
    if request.method == 'GET':
        parqueaderos = Parqueaderos.query.filter_by(estado=0, idUsuarioPar=idUsuarioPar).all()
        if not parqueaderos:
            #return jsonify({'message': 'no hay parqueaderos Inactivos'})
            return jsonify([])
        else:
            toParqueaderos = [parqueadero.getDatos() for parqueadero in parqueaderos]
            return jsonify(toParqueaderos) 


def parqueadero(idParquedero):
    #usuario = Usuarios.query.filter_by(idUsuario=idUsuario).first()
    parqueadero = Parqueaderos.query.get(idParquedero)
    if not parqueadero:
        return jsonify({'message': 'parqueadero no encontrado'})
    else:
        return jsonify(parqueadero.getDatos())

def editarParqueadero(idParquedero):
    parqueadero = Parqueaderos.query.get(idParquedero)
    if not parqueadero:
        return jsonify({'message': 'parqueadero no encontrado'})
    else:
        parqueadero.idUsuarioPar = request.json["idUsuarioPar"]
        parqueadero.direccion = request.json["direccion"]
        parqueadero.longitud = str(request.json["longitud"])
        parqueadero.latitud = str(request.json["latitud"])
        parqueadero.precio = request.json["precio"]
        parqueadero.horaApertura = request.json["horaApertura"]
        parqueadero.horaCierre = request.json["horaCierre"]
        parqueadero.puestos = request.json["puestos"]
        db.session.commit()
        return jsonify({'message': 'parqueadero actualizado con exito'})

def eliminarParqueadero(idParquedero):
    parqueadero = Parqueaderos.query.get(idParquedero)
    if not parqueadero:
        return jsonify({'message': 'parqueadero no encontrado'})
    else:
        parqueadero.estado = 0
        #db.session.delete(parqueadero)
        db.session.commit()
        return jsonify({'message': 'parqueadero eliminado con exito'})

def recuperarParqueadero(idParquedero):
    parqueadero = Parqueaderos.query.get(idParquedero)
    if not parqueadero:
        return jsonify({'message': 'parqueadero no encontrado'})
    else:
        parqueadero.estado = 1
        #db.session.delete(parqueadero)
        db.session.commit()
        return jsonify({'message': 'parqueadero recuperado con exito'})


