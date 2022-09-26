# -------------- IMPORTING THE REQUIRED MODULES -------------- #
from werkzeug.exceptions import HTTPException
import json
from flask import make_response
from utils.global_data import notAllowedCharacters
from application.models import Tracker
import datetime

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
    except ValueError:
        isValid = False
    
    return isValid

def validate_value(value,tracker_object):
    '''
    Different tracker can take different values. 
    This function checks if the value valid for the given tracker or not.
    '''
    if tracker_object.tracker_type in ["Numeric","Time Duration"]:
        for each in value:
            if not(each.isdigit() or ord(each)==ord('.')):
                return False
        return True
                
    elif tracker_object.tracker_type == "Multiple Choice":
        value_list = tracker_object.reqd_values.split(',')
        if value.strip() in value_list:
            return True
        else:
            return False
    elif tracker_object.tracker_type == "Boolean":
        if value == "True" or value == "False":
            return True
        else:
            return False

