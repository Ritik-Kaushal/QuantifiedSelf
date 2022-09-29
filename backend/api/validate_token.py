# ---------------IMPORTS---------------
from flask_restful import Resource
from utils.api_utils import Error,duplicateTracker,validate,CommaSeparated,lastEdited,latestValue
from application.models import Tracker
from database.database_config import db
import json
from utils.global_data import api_errors,tracker_list
from utils.jwt_token_utils import token_required
from flask import request,make_response


# --------------Token validation API Class--------------

class TokenValidationAPI(Resource):

    @token_required
    def get(self,**kwargs):
        make_response(json.dumps("Valid Token"),200)
