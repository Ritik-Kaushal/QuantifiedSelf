# -------------- IMPORTING THE REQUIRED MODULES -------------- #
from werkzeug.exceptions import HTTPException
import json
from flask import make_response
from utils.global_data import notAllowedCharacters
from application.models import Tracker
import datetime
from instances.cache import cache

# -------------- Error Class -------------- #

class Error(HTTPException):
    '''
    This class defines the custom errors in apis.
    params :
    1. status_code : The http status code
    2. error_msg : The message api must return when an error is encountered
    3. error_code : The custom error code api must return when an error is encountered

    '''
    def __init__(self,status_code,error_msg,error_code):
        message = {"error_code":error_code, "error_message":error_msg}
        self.response = make_response(json.dumps(message),status_code,{"Content-Type": "application/json"})




def validate(Name):
    '''
    Checks if a name entered is valid or not.
    It checks if a set of not allowed characters is present in the name or not.
    '''
    if len(Name.strip())==0:
        return False
    for char in Name:
        if char in notAllowedCharacters:
            return False
    return True

def CommaSeparated(trackerValues):
    '''
    Checks if the value is a comma separated string and has at least two options separated by a comma.
    '''
    if ',' in trackerValues:
        l = trackerValues.split(',')
        for each in l:
            if len(each.strip())==0:
                return False
        return True
    return False

def duplicateTracker(trackerName,user_id):
    '''
    Checks if a tracker for same name exists for the user or not
    '''
    trackerObj = Tracker.query.filter_by(user_id = user_id).filter_by(tracker_name = trackerName).first()
    if trackerObj:
        return True
    return False

def validate_timestamp(timestamp):
    '''
    Checks if the time stamp is valid or not
    '''
    isValid = True
    try:
        year,month,day  = timestamp[0:10].split('-')
        hours,minu,second= timestamp[11:19].split(':')
        datetime.datetime(int(year),int(month),int(day),int(hours),int(minu),int(second))
        print(hours,minu,second,year,month,day)
    except ValueError:
        isValid = False
    
    return isValid

def validate_value(value,tracker_object):
    '''
    Different tracker can take different values. 
    This function checks if the value valid for the given tracker or not.
    '''
    if tracker_object.tracker_type in ["Numerical","Time Duration"]:
        for each in value:
            if not(each.isdigit() or ord(each)==ord('.')):
                return False
        return True
                
    elif tracker_object.tracker_type == "Multiple Choice":
        value_list = tracker_object.reqd_values.split(',')
        for i in range(len(value_list)):
            value_list[i]=value_list[i].strip()
        if value.strip() in value_list:
            return True
        else:
            return False
    elif tracker_object.tracker_type == "Boolean":
        if value.strip() == "True" or value.strip() == "False":
            return True
        else:
            print(value)
            return False

def lastEdited(tracker_obj):
    log_list = tracker_obj.logs
    lastEditedTimeStamp = None
    for each in log_list:
        if lastEditedTimeStamp is None:
            lastEditedTimeStamp = each.time_stamp
        else:
            if lastEditedTimeStamp > each.time_stamp:
                lastEditedTimeStamp = each.time_stamp
    return lastEditedTimeStamp


def latestValue(tracker_obj,time_stamp):
    latest = None
    log_list = tracker_obj.logs
    for each in log_list:
        if latest is None:
            latest = each.value
        else:
            if time_stamp > each.time_stamp:
                latest = each.value
    return latest

def delete_cache(key):
    cache.delete(key)



