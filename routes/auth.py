from flask import Blueprint
from controllers import AuthController

authuser = Blueprint('authuser',__name__)

@authuser.route('/login', methods=['POST'])
def login():
    return AuthController.login()