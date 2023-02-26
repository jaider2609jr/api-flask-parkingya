from flask import Flask, jsonify, request
from utils.db import db
from routes.usuario import users
from routes.vehiculo import vehicle
from routes.parqueadero import parking
from routes.parametros import parame
from routes.detalles_parametros import deparametros
from routes.rol import roluser
from routes.auth import authuser
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/parkingya'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.register_blueprint(users)
app.register_blueprint(vehicle)
app.register_blueprint(parking)
app.register_blueprint(parame)
app.register_blueprint(deparametros)
app.register_blueprint(roluser)
app.register_blueprint(authuser)


@app.route('/')
def index():
    return jsonify({'message': 'welcome'})

def pagina_no_encontrada(error):
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"

if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    app.run(debug=True, host="0.0.0.0")
