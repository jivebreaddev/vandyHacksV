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
        self.event_interval = (end- start)/5
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
        self.api.post_ticket_class(event_id)
    def add_time(self):
        self.event_ticket.event_start += self.event_ticket.event_interval

    def add_price(self):
        self.price += self.increment
    def send_mail(self, start, end, price, url):
        pass
    def incremental_algo(self):
        for i in range(4):
            self.add_ticket_class(self.event_ticket.event_id, self.event_ticket.event_start,self.event_ticket.event_start+self.event_ticket.event_interval, self.price)
            self.send_mail(self.event_ticket.event_start,self.event_ticket.event_start+self.event_ticket.event_interval, self.price, self.event_ticket.url)
            self.add_time()
            self.add_price()
