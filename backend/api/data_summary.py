# ---------------IMPORTS---------------
from flask_restful import Resource
from utils.api_utils import Error,duplicateTracker,validate,CommaSeparated,lastEdited,latestValue
from application.models import Tracker
from database.database_config import db
import json
from utils.global_data import api_errors,tracker_list
from utils.jwt_token_utils import token_required
from flask import request,make_response
from database.cache import cache
from utils.api_cache import getDataSummary



# --------------Data Summary API Class--------------
class DataSummaryAPI(Resource):
    '''
    This is an API class for getting summary ofall trackers' logs.
    '''

    @token_required
    def get(self,**kwargs):
        '''
        This function is called when a get request comes. 

        This return the no of trackers, no of times edited,  last edited date and time
        '''
        
        user = kwargs['user']
        key = 'DataSumamry'+str(user.id)
        res = None
        if(cache.has(key)):
            print("From cache")
            res = cache.get(key)
        else:
            res = getDataSummary(user,key)
        return make_response(json.dumps(res),200)

        


