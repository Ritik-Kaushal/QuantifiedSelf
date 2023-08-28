from email.mime import application
import jwt
from functools import wraps
from flask import request
from flask import make_response
import json
from application.models import User
from flask import make_response
import jwt
from datetime import datetime,timedelta
from application.config import LocalDevelopmentConfig,ProductionConfig
import os
from dotenv import load_dotenv
load_dotenv()

secret_key=None
if(os.getenv("ENV","development")=="production"):
    pde = ProductionConfig()
    secret_key = pde.SECRET_KEY
else:
    lde = LocalDevelopmentConfig()
    secret_key = lde.SECRET_KEY


def token_required(f):
    '''
    A decorator to check the validity and correctness of the token
    '''
    @wraps(f)
    def decorated(*args, **kwargs):
        # import_app()
        token = None

        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split("Bearer ")[1]
        # return 401 if token is not passed
        if not token:
            error = {
                "error_code" : "TIM",
                "error_message" : "Token is missing !!!"
            }
            return make_response(json.dumps(error),401)
        try:
            # decoding the payload to fetch the stored details
            # data = jwt.decode(token, app.config['SECRET_KEY'])
            user = jwt.decode(token, secret_key,algorithms=["HS256"])
            current_user = User.query.filter_by(id = user['id']).first()
        except jwt.ExpiredSignatureError:
            error = {
                "error_code" : "IVT",
                "error_message" : "Invalid Token."
            }
            return make_response(json.dumps(error),400)

        # returns the current user
        kwargs['user']=current_user
        return  f(*args, **kwargs)
    return decorated

def generate_jwt_token(user):
    '''
    It generates the jwt token.\n
    Params :
        user : Object of User Class for whom token has to be generated
    '''
    jwt_token = jwt.encode({
        'id': user.id,
        'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, secret_key)
    return jwt_token