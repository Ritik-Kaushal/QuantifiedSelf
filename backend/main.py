# -------------- IMPORTING THE REQUIRED MODULES --------------- #
import os
from flask import request
from flask import Flask
from application.config import *
from flask_security import Security, SQLAlchemySessionUserDatastore
from application.models import User, Role
from flask_cors import CORS
from database.database_config import db
from flask_restful import Api
from utils.overridden.register import register
from utils.overridden.forms import ExtendedRegisterForm
import datetime

# --------------- Setting up the flask app --------------- #
app = Flask(__name__)
def create_app():
    if(os.getenv("ENV","development")=="production"):
        print("----- Starting the production development -----")
        app.config.from_object(ProductionConfig) # Configures the ProductionConfig data with the app
    else:
        print("----- Starting the local development -----")
        app.config.from_object(LocalDevelopmentConfig) # Configures the LocalDevelopmentConfig data with the app
    db.init_app(app) # A way to safely bind database handler to flask and manage connections
    api = Api(app)
    CORS(app)
    user_datastore = SQLAlchemySessionUserDatastore(db.session,User,Role)
    security = Security(app,user_datastore,register_form=ExtendedRegisterForm)
    app.app_context().push()
    return (app,api)

app,api = create_app()

@app.errorhandler(404)
def pageNotFound(e):
    return "The url doesnot exist."



# -------------- Setting the API endpoints --------------- #

from api.auth import RegisterUser,LoginUser
api.add_resource(RegisterUser,'/api/register')
api.add_resource(LoginUser,'/api/login')

from api.tracker import TrackerAPI
api.add_resource(TrackerAPI,'/api/trackers/get','/api/trackers/post','/api/trackers/delete','/api/trackers/put')

from api.trackerLogs import TrackerLogsAPI
api.add_resource(TrackerLogsAPI,'/api/trackerLogs/get','/api/trackerLogs/post','/api/trackerLogs/delete','/api/trackerLogs/put')

if __name__ == '__main__':
    app.run()