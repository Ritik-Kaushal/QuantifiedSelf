# ---------------IMPORTS---------------
from sqlite3 import Timestamp
from flask_restful import Resource
from utils.api_utils import Error,validate_timestamp,validate_value
from application.models import Tracker, TrackerLogs
from database.database_config import db
import json
from utils.global_data import api_errors
from utils.jwt_token_utils import token_required
from flask import request,make_response
import datetime
from utils.api_cache import getLogs
from database.cache import cache
from utils.api_utils import delete_cache

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

            key = "getLogs"+str(user.id)+tracker_id

            tracker_object = Tracker.query.filter_by(id = tracker_id).first()
            if tracker_object:
                if tracker_object.user_id == user.id:
                    logs_list = None
                    if(cache.has(key)):
                        print("From cache")
                        logs_list = cache.get(key)
                    else:
                        logs_list = getLogs(tracker_object,key)

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
        2. time_stamp : The timestamp when log is added (Optional)
        3. value : The value to be logged
        4. note : Some notes/details regarding the particular log (Optional)
        '''
        user = kwargs['user']
        data = request.get_json()
        if 'tracker_id' in data and data['tracker_id'] is not None and len(str(data['tracker_id']).strip())!=0:
            tracker_id = data['tracker_id']
            tracker_object = Tracker.query.filter_by(id = tracker_id).first()
            if tracker_object :
                if tracker_object.user_id == user.id :
                    time_stamp = None
                    if 'time_stamp' in data and data['time_stamp'] is not None and len(str(data['time_stamp']).strip())!=0:
                        time_stamp = data['time_stamp']
                        if not validate_timestamp(time_stamp) :
                            raise Error(status_code = 400, error_msg = api_errors["TSWF"][1], error_code = api_errors["TSWF"][0])
                    elif 'time_stamp' not in data:
                        time_stamp = datetime.datetime.now()
                    else:
                        raise Error(status_code = 400, error_msg = api_errors["TMNBN"][1], error_code = api_errors["TMNBN"][0])

                    if 'value' in data and data['value'] is not None and len(str(data['value']).strip())!=0:
                        value = data['value']
                        if validate_value(value=value,tracker_object = tracker_object):
                            note="-"
                            if 'note' in data and data['note'] is not None and len(str(data['note']).strip())!=0 :
                                note = data['note']
                            logObj = TrackerLogs(time_stamp = time_stamp,tracker_id = tracker_id,value = value,note = note)
                            db.session.add(logObj)
                            tracker_object.last_edited=time_stamp
                            tracker_object.times_edited+=1
                            db.session.commit()

                            key = "getLogs"+str(user.id)+str(tracker_id)
                            delete_cache(key)

                            return make_response(json.dumps({"message" : "Successfully Added the log.", "id":logObj.id}),200)
                        else:
                            raise Error(status_code = 400, error_msg = api_errors["TVW"][1], error_code = api_errors["TVW"][0])
                    else:
                        raise Error(status_code = 400, error_msg = api_errors["TVCN"][1], error_code = api_errors["TVCN"][0])
                else:
                    raise Error(status_code = 400, error_msg = api_errors["TNAAL"][1], error_code = api_errors["TNAAL"][0])
            else:
                raise Error(status_code = 400, error_msg = api_errors["TNF"][1], error_code = api_errors["TNF"][0])
        else:
            raise Error(status_code = 400, error_msg = api_errors["TIdR"][1], error_code = api_errors["TIdR"][0])

    @token_required
    def put(self,**kwargs):
        '''
        This function is called when a put request comes. 

        It updates tracker's logs in the database.\n
        The input is gets as json is in the following format :\n
        1. log_id : The id of the log which has to be updated
        2. time_stamp : The timestamp when log is added (Optional)
        3. value : The value to be logged
        4. note : Some notes/details regarding the particular log (Optional)
        '''
        user = kwargs['user']
        data = request.get_json()
        if 'log_id' in data and data['log_id'] is not None and len(str(data['log_id']).strip())!=0:
            log_id = data['log_id']
            logObj = TrackerLogs.query.filter_by(id=log_id).first()
            updated = []
            if logObj.tracker.user_id == user.id :

                # Checks for time stamp and updates if required
                if 'time_stamp' in data :
                    time_stamp = data['time_stamp']
                    if data['time_stamp'] is not None and len(data['time_stamp'].strip())!=0 :
                        if time_stamp != logObj.time_stamp:
                            if validate_timestamp(time_stamp) :
                                logObj.time_stamp = time_stamp
                                if logObj.tracker.last_edited < time_stamp:
                                    logObj.tracker.last_edited = time_stamp
                                updated.append("Time stamp")
                            else:
                                raise Error(status_code = 400, error_msg = api_errors["TSWF"][1], error_code = api_errors["TSWF"][0])
                    else:
                        raise Error(status_code = 400, error_msg = api_errors["TMNBN"][1], error_code = api_errors["TMNBN"][0])
                
                # Checks for value and updates if required
                if 'value' in data and data['value'] is not None and len(str(data['value']).strip())!=0:
                    value = data['value']
                    if value != logObj.value:
                        if validate_value(value=value,tracker_object = logObj.tracker):
                            logObj.value = value
                            updated.append("Value")
                        else:
                            raise Error(status_code = 400, error_msg = api_errors["TVW"][1], error_code = api_errors["TVW"][0])
                
                # Checks for notes and updates if required
                if 'note' in data :
                    note = '-'
                    if data['note'] is not None and len(str(data['note'].strip()))!=0 :
                        note = data['note']
                    if note != logObj.note:
                        logObj.note = note
                        updated.append("Note")
                if(len(updated)!=0):
                    logObj.tracker.times_edited+=1
                db.session.commit()

                key = "getLogs"+str(user.id)+str(logObj.tracker.id)
                delete_cache(key)

                return make_response(json.dumps(f"Updated : {updated}"),200)
            else:
                raise Error(status_code = 400, error_msg = api_errors["TLNAU"][1], error_code = api_errors["TLNAU"][0])
        else:
            raise Error(status_code = 400, error_msg = api_errors["TLIdR"][1], error_code = api_errors["TLIdR"][0])

    @token_required
    def delete(self,**kwargs):
        '''
        This function is called when a delete request comes. 

        It deletes the log from the database.\n
        It gets the id of log to delete as query in url as '?log_id=2'
        '''
        user = kwargs['user']
        if len(request.query_string)!=0:
            if('log_id' in request.args):
                log_id = request.args["log_id"]
                log_object = TrackerLogs.query.filter_by(id=log_id).first()
                if log_object :
                    tracker_id = str(log_object.tracker.id)
                    if log_object.tracker.user_id == user.id:
                        db.session.delete(log_object)
                        db.session.commit()

                        key = "getLogs"+str(user.id)+tracker_id
                        delete_cache(key)
                        return make_response(json.dumps('Successfully Deleted'),200)
                    else:
                        raise Error(status_code = 400, error_msg = api_errors["TLNAD"][1], error_code = api_errors["TLNAD"][0])
                else:
                    raise Error(status_code = 400, error_msg = api_errors["TLNF"][1], error_code = api_errors["TLNF"][0])
            else:
                raise Error(status_code = 400, error_msg = api_errors["IVQP"][1], error_code = api_errors["IVQP"][0])
        else:
            raise Error(status_code = 400, error_msg = api_errors["QSCBE"][1], error_code = api_errors["QSCBE"][0])