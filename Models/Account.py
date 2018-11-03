class Account:
    def __init__(self, Fname, Lname, email, phone, username, password):
        self.Fname = Fname
        self.Lname = Lname
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    def toParams(self):
        params = [self.Fname, self.Lname, self.email, self.phone, self.username, self.password]
        return params

