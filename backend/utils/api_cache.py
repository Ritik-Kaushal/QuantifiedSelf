from database.cache import cache
from utils.api_utils import Error,duplicateTracker,validate,CommaSeparated,lastEdited,latestValue

def getDataSummary(user,key):
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
    cache.set(key,res)
    return res

def getAllTrackerDetails(user,key):
    tracker_object_list = user.trackers
    result=[]
    for eachTracker in tracker_object_list:
        tempResult = {"id":eachTracker.id,
                    "tracker_name":eachTracker.tracker_name, 
                    "tracker_description":eachTracker.tracker_description,
                    "tracker_type":eachTracker.tracker_type,
                    "reqd_values" : eachTracker.reqd_values,
                    "latest_value" : None,
                    "last_edited" : eachTracker.last_edited
                    }
        if tempResult["last_edited"] is not None:
            tempResult["latest_value"] = latestValue(eachTracker,tempResult["last_edited"])
        result.append(tempResult)
    cache.set(key,result)
    return result

def getATrackerDetails(tracker_object,key):
    result = {"id":tracker_object.id,
                "tracker_name":tracker_object.tracker_name, 
                "tracker_description":tracker_object.tracker_description,
                "tracker_type":tracker_object.tracker_type,
                "reqd_values" : tracker_object.reqd_values,
                "last_edited_date" : None,
                "last_edited_time" : None,
                "reqd_values_list" : []
                }
    if result["tracker_type"] == "Multiple Choice" or result["tracker_type"] == "Boolean":
        result["reqd_values_list"] = result["reqd_values"].split(',')
    if tracker_object.last_edited is not None:
        result["last_edited_date"] = tracker_object.last_edited[:10]
        result["last_edited_time"] = tracker_object.last_edited[11:]
    cache.set(key,result)
    return result

def getLogs(tracker_object,key):
    reqd_logs = tracker_object.logs
    logs_list = []
    for eachLog in reqd_logs:
        result = {"id":eachLog.id,
                "time_stamp":eachLog.time_stamp, 
                "value":eachLog.value,
                "note":eachLog.note
                }
        logs_list.append(result)
    cache.set(key,logs_list)
    return logs_list

