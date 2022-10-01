import csv
import os
from database.create_app import app

def convert_to_csv(user):
    dir = app.config["SQLITE_DB_DIR"]
    os.chdir(dir)
    tracker_list = user.trackers
    file_list = []
    for tracker in tracker_list:
        try:
            file_name = str(user.id)+"tracker-"+tracker.tracker_name+".csv"
            with open(file_name,'w',newline='') as file:
                file_list.append(file_name)
                writer = csv.writer(file)

                name = ["Tracker Name", tracker.tracker_name]
                writer.writerow(name)

                tracker_type = ["Tracker Type", tracker.tracker_type]
                writer.writerow(tracker_type)

                tracker_description = ["Tracker Description", tracker.tracker_description]
                writer.writerow(tracker_description)

                tracker_values = ["Tracker Values", tracker.reqd_values]
                writer.writerow(tracker_values)

                empty_row = []
                writer.writerow(empty_row)

                log_list = tracker.logs
                if len(log_list) != 0:
                    title = ["Timestamp", "Value", "Note"]
                    writer.writerow(title)
                    for log in log_list:
                        log_data = [log.time_stamp, log.value, log.note]
                        writer.writerow(log_data)

                    empty_row = []
                    writer.writerow(empty_row)           
        except:
            for each in file_list:
                os.remove(each)
            return []

                  

    return file_list
