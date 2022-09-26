api_errors = {
    # Common
    'CTA/J' : ["COMMON001","Request Content-Type must be 'application/json'"],
    'IVQP' : ["COMMON002","Invalid Query Parameter"],
    'QSCBE' : ["COMMON003", "Query String cannot be empty"],

    # Login API
    'INVPASS' : "Invalid Password",
    'MIDET' : "Missing Details",
    'USRNF' : "User not found",

    # Tracker API
    "TNF" : ["TRACKER000", "Tracker not found for this tracker id"],
    "TNaR" : ["TRACKER001", "Tracker Name is required"],
    "TNaNA" : ["TRACKER002", "Tracker Name can not contain special characters except underscore"],
    "TVaNA" : ["TRACKER003", "Tracker Value must contain at least 2 value separated by comma"],
    "TVaR" : ["TRACKER004", "Tracker Value is required"],
    "TNAV" : ["TRACKER005", "You are not authorised to view this tracker"],
    "TNAU" : ["TRACKER006", "You are not authorised to update this tracker"],
    "TNAD" : ["TRACKER007", "You are not authorised to delete this tracker"],
    "TNaI" : ["TRACKER008", "Tracker Name must be unique for a user"],
    "TTR" : ["TRACKER009", "Tracker Type is required"],
    "TNIL" : ["TRACKER010", "Tracker Name is not in List"],
    "TIdR" : ["TRACKER011", "Tracker Id is required"],

    # Tracker Logs
    "TNAAL" : ["LOG000","You are not authorised to add log of this tracker"],
    "TNAUL" : ["LOG001","You are not authorised to view log of this tracker"],
    "TMNBN" : ["LOG002","Time Stamp(if present) must not be null or empty"],
    "TSWF" : ["LOG003","Time Stamp is in wrong format"],
    "TVCN" : ["LOG004","Tracker Value is required"],
    "TVW" : ["LOG005","Tracker Value is wrong"],
    "TLNF" : ["LOG006","Log not found"],
    "TLNAU" : ["LOG007","You are not authorised to update log of this tracker"],
    "TLNAD" : ["LOGT008", "You are not authorised to delete this log of this tracker"],
    "TLIdR" : ["LOGT009", "Log id is required"]
    
}

notAllowedCharacters = ['*','@',':',',','/','[','?',']','|','\\','"','<','>','+',';','(',')','{','}','&','%','$','!','^','.']

tracker_list = ['Multiple Choice','Numeric','Time Duration','Boolean']