from database.celery_setting import cel

# -------------- Setting Celery Tasks --------------- #
from celery.schedules import crontab

@cel.on_after_configure.connect
def setup_periodic_tasks(sender,**kwargs):
    sender.add_periodic_task(crontab(hour=18, minute=0),remainder_emails.s(),name="A remainder email to all those who have not updated the logs today")
    sender.add_periodic_task(10,email_reports.s(),name="A report is emailed to all the users.")


from utils.mail_sender.remainder_mail import send_remainder_emails
@cel.task(name="send remainder emails")
def remainder_emails():
    send_remainder_emails()
    
from utils.mail_sender.reports_mail import send_reports_emails_all
@cel.task(name="send reports")
def email_reports():
    send_reports_emails_all()

from utils.mail_sender.export_mail import export_data_and_mail
@cel.task(name="export")
def export_data(user_id):
    print("In task")
    (output,message) = export_data_and_mail(user_id)
    return (output,message)


