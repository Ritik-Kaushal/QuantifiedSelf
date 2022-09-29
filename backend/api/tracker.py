# ---------------IMPORTS---------------
from flask_restful import Resource
from utils.api_utils import Error,duplicateTracker,validate,CommaSeparated,lastEdited,latestValue
from application.models import Tracker
from database.database_config import db
import json
from utils.global_data import api_errors,tracker_list
from utils.jwt_token_utils import token_required
from flask import request,make_response
import datetime
from utils.api_cache import getAllTrackerDetails,getATrackerDetails
from database.cache import cache
from utils.api_utils import delete_cache
# --------------Tracker API Class--------------
class TrackerAPI(Resource):
    '''
    This is an API class for operations on the trackers.
    '''
    @token_required
    def get(self,**kwargs):
        '''
        This function is called when a get request comes. 

        It has two types of output :     

            1. When no query parameter is passed, it will return a list of all trackers of the invoking user.
            2. If a query parameter i.e. '?tracker_id=2' is passed in url, then, it will return the details of tracker whose id is 2.
        '''
        user = kwargs['user']
        if len(request.query_string)==0:
            key = "getAllTrackerDetails"+str(user.id)
            result = None
            if(cache.has(key)):
                print("From cache")
                result = cache.get(key)
            else:
                result = getAllTrackerDetails(user,key)
            return make_response(json.dumps(result),200)

        elif('tracker_id' in request.args):
            tracker_id = str(request.args['tracker_id'])
            key = "getOneTrackerDetail"+str(user.id)+tracker_id
            tracker_object = Tracker.query.filter_by(id = tracker_id).first()
            if tracker_object:
                if tracker_object.user_id == user.id:
                    result = None
                    if(cache.has(key)):
                        print("From cache")
                        result = cache.get(key)
                    else:
                        result = getATrackerDetails(tracker_object,key)
                    return make_response(json.dumps(result),200)
                else:
                    raise Error(status_code = 401, error_msg = api_errors["TNAV"][1], error_code = api_errors["TNAV"][0])
            else:
                raise Error(status_code = 404, error_msg = api_errors["TNF"][1], error_code = api_errors["TNF"][0])
        else:
            raise Error(status_code = 404, error_msg = api_errors["IVQP"][1], error_code = api_errors["IVQP"][0])

    @token_required
    def post(self,**kwargs):
        '''
        It adds tracker data to the database.\n
        The input is gets as json is in the following format :\n
        1. tracker_name : The name of the tracker
        2. tracker_type : The type of the tracker
        3. tracker_description : Some details about the tracker (optional)
        4. tracker_values : The values of the tracker (only in case of Multiple Choice Tracker)
        '''
        user = kwargs['user']
        data = request.get_json()
        print(data)
        if 'tracker_name' in data and data['tracker_name'] is not None :
            trackerName = data['tracker_name']
            if not duplicateTracker(trackerName,user.id):
                if validate(trackerName):
                    if 'tracker_type' in data and data['tracker_type'] is not None:
                        trackerType = data['tracker_type']
                        if trackerType in tracker_list:  
                            trackerDescription = None
                            if 'tracker_description' in data and data['tracker_description'] is not None:
                                trackerDescription = data['tracker_description']  
                            tracker_object = Tracker(tracker_name = trackerName, tracker_description = trackerDescription, tracker_type = trackerType, reqd_values = None, user_id = user.id)
                            
                            if trackerType == "Multiple Choice" :
                                if 'tracker_values' in data and data['tracker_values'] is not None :
                                    trackerValues = data['tracker_values']  # Only applicable for multiple choice tracker
                                    if(CommaSeparated(trackerValues)):
                                        tracker_object.reqd_values = trackerValues
                                    else:
                                        raise Error(status_code = 400, error_msg = api_errors["TVaNA"][1], error_code = api_errors["TVaNA"][0])
                                else:
                                    raise Error(status_code = 400, error_msg = api_errors["TVaR"][1], error_code = api_errors["TVaR"][0])
                            if trackerType == "Boolean" :  
                                tracker_object.reqd_values = "True, False"      
                            db.session.add(tracker_object)
                            db.session.commit()

                            # When a new tracker is added, get all tracker cache has to be deleted. 
                            key = "getAllTrackerDetails"+str(user.id)
                            delete_cache(key)
                            
                            result = {"message" : "Tracker Successfully added","id" : tracker_object.id}
                            return make_response(json.dumps(result),200) 
                        else:
                            raise Error(status_code = 400, error_msg = api_errors["TNIL"][1], error_code = api_errors["TNIL"][0])         
                    else:
                        raise Error(status_code = 400, error_msg = api_errors["TTR"][1], error_code = api_errors["TTR"][0])
                else:
                    raise Error(status_code = 400, error_msg = api_errors["TNaNA"][1], error_code = api_errors["TNaNA"][0])
            else:
                raise Error(status_code = 400, error_msg = api_errors["TNaI"][1], error_code = api_errors["TNaI"][0]) 
        else:
            raise Error(status_code = 400, error_msg = api_errors["TNaR"][1], error_code = api_errors["TNaR"][0])

    @token_required
    def put(self,**kwargs):
        '''
        It updates tracker data in the database.\n
        The input is gets as json is in the following format :\n
        1. tracker_id : The id of tracker to edit (Compulsory)
        2. tracker_name : The name of the tracker (Optional)
        3. tracker_description : Some details about the tracker (optional)
        4. tracker_values : The values of the tracker (only in case of Multiple Choice Tracker) (Optional)
        '''
        user = kwargs['user']
        data = request.get_json()
        if 'tracker_id' in data and data['tracker_id'] is not None and len(str(data['tracker_id']).strip())!=0:
            tracker_id = str(data['tracker_id'])
            tracker_object = Tracker.query.filter_by(id=tracker_id).first()
            updated = []
            if tracker_object.user_id == user.id :
                if 'tracker_name' in data :
                    trackerName = data['tracker_name']
                    if data['tracker_name'] is not None and len(data['tracker_name'].strip())!=0 :
                        if trackerName != tracker_object.tracker_name :
                            if not duplicateTracker(trackerName,user.id):
                                if validate(trackerName):
                                    tracker_object.tracker_name = trackerName
                                    updated.append("Tracker Name")
                                else:
                                    raise Error(status_code = 400, error_msg = api_errors["TNaNA"][1], error_code = api_errors["TNaNA"][0])
                            else:
                                raise Error(status_code = 400, error_msg = api_errors["TNaI"][1], error_code = api_errors["TNaI"][0])
                    else:
                        raise Error(status_code = 400, error_msg = api_errors["TNaR"][1], error_code = api_errors["TNaR"][0])
                
                if 'tracker_description' in data:
                    trackerDescription = data['tracker_description']
                    tracker_object.tracker_description = trackerDescription
                    updated.append("Tracker Description")

                if 'tracker_values' in data :
                    if tracker_object.tracker_type == "Multiple Choice":
                        if data['tracker_values'] is not None:
                            trackerValues = data['tracker_values']
                            if(CommaSeparated(trackerValues)):
                                tracker_object.reqd_values = trackerValues
                                updated.append("Required Values")  
                            else:
                                raise Error(status_code = 400, error_msg = api_errors["TVaNA"][1], error_code = api_errors["TVaNA"][0])
                        else:
                            raise Error(status_code = 400, error_msg = api_errors["TVaR"][1], error_code = api_errors["TVaR"][0])
                db.session.commit()

                # When a tracker is edited, get all tracker cache as well as get one tracker cache has to be deleted. 
                key1 = "getAllTrackerDetails"+str(user.id)
                delete_cache(key1)

                key2 = "getOneTrackerDetail"+str(user.id)+tracker_id
                delete_cache(key2)

                result = {"message" : "Tracker Successfully Updated","id" : tracker_object.id}
                return make_response(json.dumps(result),200)
            else:
                raise Error(status_code = 400, error_msg = api_errors["TNAU"][1], error_code = api_errors["TNAU"][0])
        else:
            raise Error(status_code = 400, error_msg = api_errors["TIdR"][1], error_code = api_errors["TIdR"][0])
        
    @token_required
    def delete(self,**kwargs):
        '''
        It deletes the tracker and its related logs from the database.\n
        It gets the id of tracker to delete as query in url as '?tracker_id=2'
        '''
        user = kwargs['user']
        if len(request.query_string)!=0:
            if('tracker_id' in request.args):
                tracker_id = str(request.args["tracker_id"])
                tracker_object = Tracker.query.filter_by(id=tracker_id).first()
                if tracker_object :
                    if tracker_object.user_id == user.id:
                        db.session.delete(tracker_object)
                        db.session.commit()

                        # When a tracker is deleted, get all tracker cache as well as get one tracker cache has to be deleted. 
                        key1 = "getAllTrackerDetails"+str(user.id)
                        delete_cache(key1)

                        key2 = "getOneTrackerDetail"+str(user.id)+tracker_id
                        delete_cache(key2)

                        return make_response(json.dumps('Successfully Deleted'),200)
                    else:
                        raise Error(status_code = 400, error_msg = api_errors["TNAD"][1], error_code = api_errors["TNAD"][0])
                else:
                    raise Error(status_code = 400, error_msg = api_errors["TNF"][1], error_code = api_errors["TNF"][0])
            else:
                raise Error(status_code = 400, error_msg = api_errors["IVQP"][1], error_code = api_errors["IVQP"][0])
        else:
            raise Error(status_code = 400, error_msg = api_errors["QSCBE"][1], error_code = api_errors["QSCBE"][0])