class Student:
    school_name = "Semicolon Institute"
    website = "semicolon.africa"
    tuition_fee_increase_per_level = 1.04
    number_of_students = 0


    def __init__(self, firstname, lastname, phone_number, age, email, registration_number,id_number, tuition_fee, roll_number):
        self.firstname = firstname
        self.lastname = lastname
        self.phoneNumber = phone_number
        self.age = age
        self.registration_number = registration_number
        self.id_number = id_number
        self.tuition_fee = 1000000

# using property decorator
# a getter function
    @property
    def fullname(self):
        return f"{self.firstname}{self.lastname}"
    @property
    def email(self):
        return f"{self.firstname}.{self.lastname} + @gmail.com"
    @property
    def age(self):
        return self.age

# a setter function
    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split(" ")
        self.firstname = firstname
        self.lastname = lastname

# a deleter function
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.firstname = None
        self.lastname = None

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Sorry your age is below eligibility criteria")
        self.age = age

    def display_phone_number(self):
        return self.phoneNumber
    def display_registration_number(self):
        return self.registration_number
    def display_id_number(self):
        return self.id_number

student1 = Student()
student2 = Student()
