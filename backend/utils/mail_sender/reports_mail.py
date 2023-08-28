from utils.report_generator.report_generator import generate_PDF_report
from application.models import User
from utils.mail_sender.mail import sendMail
import os
import time
from create_app import app

def send_reports_emails_all():
    dir = app.config["SQLITE_DB_DIR"]
    os.chdir(dir)
    try:
        user_list = User.query.all()
        for user in user_list:
            generate_PDF_report(user,'Monthly')
            out = sendMail(user.email,"Your Monthly report from Track It","Find your report attached below",f'{user.email}_report.pdf')
            time.sleep(30)
    except :
        return False

    
    for user in user_list:
        file_name = f'{user.email}_report.pdf'
        os.remove(file_name)
