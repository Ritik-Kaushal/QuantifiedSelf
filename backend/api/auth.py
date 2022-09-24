# -------------- IMPORTING THE REQUIRED MODULES -------------- #
from flask import request,jsonify
from flask_restful import Resource
from application.models import User
from utils.overridden.register import register
from flask_security.utils import verify_password
from utils.jwt_token_utils import generate_jwt_token
from utils.api_utils import Error
from utils.global_data import api_errors


# -------------- Register API -------------- #
class RegisterUser(Resource):
    '''
    An api class to register user using flask security.\n
    No parameters required.\n
    No authentication required.\n
    '''

    def post(self):
        response = register()
        return response

# -------------- Login API -------------- #
class LoginUser(Resource):
    '''
    An api class to login user by generating jwt_token valid for a specified time duration.\n
    No parameters required.\n
    No authentication required.\n
    '''

    def post(self):
        email = None
        password = None
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
        except:
            raise Error(status_code = 401, error_msg = api_errors["CTA/J"][1], error_code = api_errors["CTA/J"][0])

        if(email is not None and password is not None):
            user = User.query.filter_by(email=email).first()
            if user is not None:
                if verify_password(password,user.password):
                    jwt_token = generate_jwt_token(user)
                    return jsonify({'jwt_token' : jwt_token})
                else:
                    raise Error(400,api_errors['INVPASS'],"INVPASS")
            else:
                raise Error(400,api_errors['USRNF'],"USRNF")
        else:
            raise Error(400,api_errors['MIDET'],"MIDET")

