# -------------- IMPORTING THE REQUIRED MODULES --------------- #
import os
from application.config import *
from instances.database_config import db
from flask_security import Security, SQLAlchemySessionUserDatastore
from application.models import User, Role
from flask_cors import CORS
from flask_restful import Api
from utils.overridden.forms import ExtendedRegisterForm
from instances.cache import cache
from instances.celery_setting import cel
from create_app import app
from instances.mail_create import mail

from dotenv import load_dotenv
load_dotenv()


# --------------- Setting up the flask app --------------- #
def create_app():
    if(os.getenv("ENV","Development")=="Production"):
        print("----- Starting the production development -----")
        app.config.from_object(ProductionConfig) # Configures the ProductionConfig data with the app
    else:
        print("----- Starting the local development -----")
        app.config.from_object(LocalDevelopmentConfig) # Configures the LocalDevelopmentConfig data with the app

    # Configuring Celery
    cel.conf.broker_url = app.config["BROKER"]
    cel.conf.result_backend = app.config["BACKEND"]
    cel.conf.enable_utc = app.config["ENABLE_UTC"]
    cel.conf.timezone = app.config["TIMEZONE"]

    class ContextTask(cel.Task):
        def __call__(self,*args,**kwargs):
            with app.app_context():
                return self.run(*args,**kwargs)

    cel.Task = ContextTask


    db.init_app(app) # A way to safely bind database handler to flask and manage connections
    api = Api(app)
    cache.init_app(app)
    CORS(app)
    user_datastore = SQLAlchemySessionUserDatastore(db.session,User,Role)
    security = Security(app,user_datastore,register_form=ExtendedRegisterForm)
    mail.init_app(app)
    app.app_context().push()

    return (app,api,mail,cache,cel)

app,api,mail,cache,cel = create_app()

# def initializeDatabase():
#     with app.app_context():
#         inspector = db.inspect(db.engine)
#         table_names = inspector.get_table_names()

#         if not table_names: 
#             # If no tables exist
#             db.create_all()
#             print("Database tables created.")
#         else:
#             pass

@app.route('/recovered')
def post_recovery():
    return "Successfully Recovered. Close this tab and login again."

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

from api.exportAPI import ExportAPI
api.add_resource(ExportAPI,'/api/exportData')


from utils.celery.tasks import *

if __name__ == '__main__':
    # initializeDatabase()
    app.run(port=5000)