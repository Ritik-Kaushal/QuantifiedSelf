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
from flask_mail import Mail,Message

# --------------- Setting up the flask app --------------- #
def create_app():
    app = Flask(__name__)
    
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
    mail= Mail(app)
    app.app_context().push()
    return (app,api,mail)

app,api,mail = create_app()



@app.route("/")
def index():
    from utils.mail_sender.report_mail import sendMail
    sendMail('emailinflaskbyritik@gmail.com','ritikkaushallvb@gmail.com',"Testing from function",'Hello This is a testing mail','report.pdf')

    return "done"

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

from api.validate_token import TokenValidationAPI
api.add_resource(TokenValidationAPI,'/api/tokenValidation/get')

from api.data_summary import DataSummaryAPI
api.add_resource(DataSummaryAPI,'/api/dataSummary/get')


if __name__ == '__main__':
    app.run()