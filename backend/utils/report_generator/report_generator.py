from datetime import date
from application.models import User
from table_generator import TableCreator

class PDF(TableCreator):
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
    
    def add_title(self,title,subtitle):
        # pdf.cell(cell width,cell height,text_to_add, ln = True,,border=True) ln means new line
        self.set_font('helvetica','BIU',20)
        self.cell(190,20,title,align='C')
        self.ln(8)
        self.cell(190,20,subtitle,align='C')

    def add_heading(self,heading,x1,y1,x2,y2):
        self.ln(20)
        self.set_font('helvetica','B',18)
        self.cell(190,15,heading,ln=True)
        self.line(x1,y1,x2,y2)

    def add_user_details(self,name,email):
        self.set_font('helvetica','',14)
        self.cell(190,10,'User Name : {0}'.format(name))
        self.ln(8)
        self.set_font('helvetica','',14)
        self.cell(190,10,'User Email : {0}'.format(email))
    
    def add_tracker_details(self,tracker_dict):
        self.ln(10)
        self.set_font('helvetica','BI',16)
        self.cell(190,10,'{0}'.format(tracker_dict['tracker_name']),align='C')
        self.ln(8)
        self.set_font('helvetica','',14)
        self.cell(190,10,'Tracker Type : {0}'.format(tracker_dict['tracker_type']))
        self.ln(8)
        self.set_font('helvetica','',14)
        self.cell(190,10,'Tracker Description : {0}'.format(tracker_dict['tracker_description']))
        if tracker_dict['tracker_values'] is not None:
            self.ln(8)
            self.set_font('helvetica','',14)
            self.cell(190,10,'Tracker Values : {0}'.format(tracker_dict['tracker_values']))
        self.ln(10)

        data_reqd = [['S.N.','Time stamp','Value','Note']] + tracker_dict['logs']
        table_title = 'Logs for {0} tracker'.format(tracker_dict['tracker_name'])
        self.set_font('helvetica','B',14)
        self.cell(190,15,table_title,ln=True)
        self.create_table(table_data=data_reqd,data_size=12,title_size=14,align_data='C',align_header='C',cell_width=[20,50,20,100])
           


def getData(user_object):
    data_dict = {}
    data_dict["name"] = user_object.name
    data_dict["email"] = user_object.email
    tracker_object_list = user_object.trackers
    data_dict["tracker_list"] = [] # It will contaain dictionaries of trackers
    
    for eachTracker in tracker_object_list:
        tracker = {}
        tracker["tracker_name"] = eachTracker.tracker_name
        tracker["tracker_description"] = eachTracker.tracker_description
        tracker["tracker_type"] = eachTracker.tracker_type
        tracker["tracker_values"] = eachTracker.reqd_values
        tracker["logs"] = [] # It will contain list of logs
        log_object_list = eachTracker.logs
        i=1
        for eachLog in log_object_list:
            log = []
            log.append(i)
            i+=1
            log.append(eachLog.time_stamp)
            log.append(eachLog.value)
            log.append(eachLog.note)
            tracker["logs"].append(log)
        data_dict["tracker_list"].append(tracker)
    return data_dict


def generate_PDF_report(user,type="Monthly"): # user object and type of report (monthly or weekly)
    global title
    data = getData(user)
    today = date.today()
    month, year = (today.month-1, today.year) if today.month != 1 else (12, today.year-1)
    prev_month = today.replace(day=1, month=month, year=year)
    title = "{0} report of {1} ".format(type,data["name"])
    subtitle = "{0} to {1}".format(prev_month,today)

    pdf = PDF('P','mm','A4')
    pdf.set_auto_page_break(auto=True,margin=10)
    pdf.add_page()
    pdf.set_margins(10,10,10)

    pdf.add_title(title,subtitle)

    pdf.add_heading('User Details',10,50, 190, 50)
    pdf.add_user_details(data['name'],data['email'])

    pdf.add_heading('Trackers',10,93, 190, 93)
    pdf.set_font('helvetica','',14)
    pdf.cell(190,10,'Following are the trackers with their logs : ')
    pdf.ln(10)
    for i in range(len(data['tracker_list'])):
        tracker_dict = data['tracker_list'][i]
        pdf.add_tracker_details(tracker_dict)

    

    
    pdf.output('report.pdf', 'F')
