class Account:

    def __init__(self, firstname, lastname, email, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.email = email
        if balance > 0.0:
            self.balance = balance
