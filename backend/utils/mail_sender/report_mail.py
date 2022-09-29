from main import mail,app
from flask_mail import Message

def sendMail(SENDER_ADDRESS,RECEIVER_ADDRESS,SUBJECT,MESSAGE,ATTACHMENT=None):
    msg = Message(recipients=[RECEIVER_ADDRESS],
                  sender=SENDER_ADDRESS,
                  body=MESSAGE,
                  subject=SUBJECT)
    with app.open_resource(ATTACHMENT) as fp:
        msg.attach(f"{RECEIVER_ADDRESS}_report.pdf", "application/pdf", fp.read())
    mail.send(msg)


    