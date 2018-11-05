import time
import urllib
from datetime import datetime
import sendgrid
from sendgrid import Email
from sendgrid.helpers.mail import Content, Mail


class Account:
    def __init__(self, Fname, Lname, email, phone, username, password, oAuth):
        self.Fname = Fname
        self.Lname = Lname
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password
        self.oAuth = oAuth

    def toParams(self):
        params = [self.Fname, self.Lname, self.email, self.phone, self.username, self.password, self.oAuth]
        return params

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Event:
    def __init__(self, name, date, location, price):
        self.name = name
        self.date = date
        self.location = location
        self.price = price

class event_ticket:
    event_id = None
    event_ticket_list = {}
    user_id = None
    name = None
    event_start= None
    event_end = None
    event_interval = None
    url = None
    def __init__(self, event_id, user_id):
        self.event_id = event_id
        self.user_id = user_id


    def event_time_load(self, start, end):
        self.event_start = start
        self.event_end = end
        self.event_interval = (end - start)/10
    def event_details(self,name, url):
        self.name = name['text']
        self.url = url

class algo:
    event_ticket = None
    price = None
    increment = None
    api = None
    def __init__(self, price,increment, event_ticket, api):
        self.price = price
        self.increment = increment
        self.event_ticket = event_ticket
        self.api = api
    def add_ticket_class(self, event_id, start, end, price):
        self.api.post_ticket_class(event_id,name="jason", quantity_total= 10 ,cost= price, sales_start= start, sales_end=end)
    def add_time(self):
        self.event_ticket.event_start += self.event_ticket.event_interval

    def add_price(self):
        self.price += self.increment

    def send_mail(self, start, end, price, url):

        sg = sendgrid.SendGridAPIClient(apikey='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')
        from_email = Email("sbhandari155708@troy.edu")
        subject = "This is a test email."
        to_email = Email("spark@troy.edu")
        content = Content('text/html', 'text')
        mail = Mail(from_email, subject, to_email, content)
        name = "Sichang Park"
        dynamic_template_data = {
            'name': name, "price": price, "date": "Denver", "firstName": name, 'url': url
        }
        # unixtime = time.mktime(end.timetuple())
        # mail.send_at = unixtime
        mail.personalizations[0].dynamic_template_data = dynamic_template_data
        mail.template_id = "d-c9c69c9a4d164310a1c5f3c289b9d93c"
        try:
            sg.client.mail.send.post(request_body=mail.get())
        except:
            pass


    def incremental_algo(self):
        for i in range(4):
            self.add_ticket_class(self.event_ticket.event_id, self.event_ticket.event_start,self.event_ticket.event_start+self.event_ticket.event_interval, self.price)
            self.send_mail(self.event_ticket.event_start,self.event_ticket.event_start+self.event_ticket.event_interval, self.price, self.event_ticket.url)
            self.add_time()
            self.add_price()
