import email
from email import message
from application.models import User
from utils.mail_sender.mail import sendMail
import time
import datetime

def send_remainder_emails():
    try:
        last_timestamp =  str(datetime.datetime.now()-datetime.timedelta(1))[0:19]
        userList = User.query.all()
        for user in userList:
            if(user.confirmed_at and user.active):
                trackers_list = user.trackers
                if(len(trackers_list)==0):
                    message = "You have not added any trackers yet. Do add asap."
                    sendMail(user.email,"Remainder for adding trackers.",message)
                    time.sleep(30)
                else:
                    not_logged = []
                    for tracker in trackers_list :
                        if tracker.last_edited < last_timestamp:
                            not_logged.append(tracker.tracker_name)

                    message = "You have not logged any data today for the given trackers - "

                    for i in range(len(not_logged)-1):
                        message+=not_logged[i]+", "
                    message+=not_logged[-1]+'.'

                    sendMail(user.email,"Remainder for Logging in the data for various trackers.",message)
                    time.sleep(30)
    except:
        return False


