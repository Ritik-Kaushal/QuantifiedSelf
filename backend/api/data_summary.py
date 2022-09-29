# ---------------IMPORTS---------------
from flask_restful import Resource
from utils.api_utils import Error,duplicateTracker,validate,CommaSeparated,lastEdited,latestValue
from application.models import Tracker
from database.database_config import db
import json
from utils.global_data import api_errors,tracker_list
from utils.jwt_token_utils import token_required
from flask import request,make_response


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
        tracker_list = user.trackers
        res = {
            'no_of_trackers' : len(tracker_list),
            "no_of_times_edited" : 0,
            "last_edited_date" : None,
            "last_edited_time" : None
        }

        count = 0
        last_edited_timestamp = None
        for each in tracker_list:
            print(each.last_edited,last_edited_timestamp)
            if each.last_edited and last_edited_timestamp is None:
                last_edited_timestamp = each.last_edited
            elif each.last_edited and last_edited_timestamp < each.last_edited:
                last_edited_timestamp = each.last_edited
            count+=each.times_edited
        res["no_of_times_edited"] = count
        if last_edited_timestamp is None:
            res["last_edited_date"] =  None
            res["last_edited_time"] =  None
        else:
            res["last_edited_date"] = last_edited_timestamp[:10]
            res["last_edited_time"] = last_edited_timestamp[11:]
        print(res)
        return make_response(json.dumps(res),200)

        


