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

