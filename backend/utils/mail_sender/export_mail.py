from import_export.convertor import convert_to_csv
from import_export.zip_unzip import zip_files
from utils.mail_sender.mail import sendMail
from application.models import Tracker, User

def export_data_and_mail(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is not None:
        tracker_list = user.trackers
        if len(tracker_list)!=0:
            file_list = convert_to_csv(user)
            if len(file_list)!=0:
                zip_file_path = zip_files(user.id,file_list)
                if zip_file_path:
                    print(zip_file_path)
                    out = sendMail(RECEIVER_ADDRESS= user.email,SUBJECT= "Your Exported Data", MESSAGE= "Here is the exported data attached.",ATTACHMENT = zip_file_path,mime_type="application/x-zip")
                    if not out:
                        return (False,"Could not send the email")
                    else:
                        return (True, "Successfully exported and sent the email.")
                else:
                    return (False, "Could not convert to zip")
            else:
                return (False, "Could not convert to csv")
    else:
        return (False,"User not found")