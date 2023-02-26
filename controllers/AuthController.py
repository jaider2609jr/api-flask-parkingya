from flask import jsonify, request
from models.Usuario import *
import jwt
import datetime
key='secret_key_parking'

def login():
    username = request.json["username"]
    password = request.json["password"]
    if request.method == 'POST':
        usuario = Usuarios.query.filter_by(username=username).first()
        if not usuario:
            return jsonify({
                'message': 'usuario invalido',
                'status': 'not_found',
            })
        else:
            if usuario.password != password:
                return jsonify({
                    'message': 'contraseña incorrecta',
                    'status': 'error_password'
                    })
            else:
                token = jwt.encode({'public_id':usuario.idUsuario, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},key)
                return jsonify({
                    'message': 'Bienvenido a parkingYa '+username,
                    'status':'ok',
                    'user_id':usuario.idUsuario,
                    'token':token
                    })


