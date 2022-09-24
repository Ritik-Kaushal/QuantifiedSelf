# ---------------IMPORTS---------------
from flask_restful import Resource
from utils.api_utils import Error,duplicateTracker,validate,CommaSeparated
from application.models import Tracker
from database.database_config import db
import json
from utils.global_data import api_errors,tracker_list
from utils.jwt_token_utils import token_required
from flask import request,make_response


# --------------Tracker Logs API Class--------------
class TrackerLogsAPI(Resource):
    '''
    This is an API class for operations on the tracker's logs.
    '''

    @token_required
    def get(self,**kwargs):
        '''
        This function is called when a get request comes. 

        A query parameter i.e. '?tracker_id=2' has to be passed in url. It will return the logs of tracker whose id is 2.
        '''
        user = kwargs['user']
        if len(request.query_string)==0:
            raise Error(status_code = 400, error_msg = api_errors["QSCBE"][1], error_code = api_errors["QSCBE"][0])
        elif('tracker_id' in request.args):
            tracker_id = str(request.args['tracker_id'])
            tracker_object = Tracker.query.filter_by(id = tracker_id).first()
            if tracker_object:
                if tracker_object.user_id == user.id:
                    reqd_logs = tracker_object.logs
                    logs_list = []
                    for eachLog in reqd_logs:
                        result = {"id":eachLog.id,
                                "time_stamp":eachLog.time_stamp, 
                                "value":eachLog.value,
                                "note":eachLog.note
                                }
                        logs_list.append(result)
                    return make_response(json.dumps(logs_list),200)
                else:
                    raise Error(status_code = 401, error_msg = api_errors["TNAV"][1], error_code = api_errors["TNAV"][0])
            else:
                raise Error(status_code = 404, error_msg = api_errors["TNF"][1], error_code = api_errors["TNF"][0])
        else:
            raise Error(status_code = 404, error_msg = api_errors["IVQP"][1], error_code = api_errors["IVQP"][0])

    @token_required
    def post(self,**kwargs):
        '''
        This function is called when a post request comes. 

        It adds tracker's logs to the database.\n
        The input is gets as json is in the following format :\n
        1. tracker_id : The id of the tracker whose logs is to be added
        2. time_stamp : The timestamp when log is added
        3. value : The value to be logged
        4. note : Some notes/details regarding the particular log (Optional)
        '''
        user = kwargs['user']
        data = request.get_json()
        if 'tracker_id' in data and data['tracker_id'] is not None and len(str(data['tracker_id'].strip()))!=0:
            tracker_id = data['tracker_id']
        else:
            raise Error(status_code = 400, error_msg = api_errors["TIdR"][1], error_code = api_errors["TIdR"][0])
