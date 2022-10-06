class Employee:

## Instance Methods:
    def __init__(self, firstname, lastname, age, salary, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + "." + lastname
        self.age = age
        self.phone_number = phone_number
        self.salary = salary
        self.email = firstname + lastname + "@gmail.com"
# Note: We didn't pass in fullname and email as an argument because we can create them using first name and last name.
    def display_firstname(self):
        return self.firstname
    def display_lastname(self):
        return self.lastname
    def display_fullname(self):
        return self.fullname
    def display_email(self):
        return self.email
    def display_age(self):
        return self.age
    def display_salary(self):
        return self.salary
    def display_phone_number(self):
        return self.phone_number


## Class Methods:

    @classmethod
    def set_salary_raise_amount(cls, raise_amount):
        cls.salary_raise_amount = raise_amount



### Object Creation
employee1 = Employee("Jude", "Onyedeke", 24, 1000000, "08181615310")
employee2 = Employee("Ekpei", "Raphael", 29, 500000, "09093837491")

## Method Call
print(f"Employee1 information:\nfirstname: {employee1.display_firstname()}\nlastname: {employee1.display_lastname()}\nfullname: {employee1.display_fullname()}\n email: {employee1.display_email()}\nage: {employee1.display_age()}\n"
      f"phone number: {employee1.display_phone_number()}\nsalary: {employee1.display_salary()}\nsalary_raise: {employee1.display_salary_raise()}")

print(f"Employee2 information:\nfirstname: {employee2.display_firstname()}\nlastname: {employee2.display_lastname()}\nfullname: {employee2.display_fullname()}\n email: {employee2.display_email()}\nage: {employee2.display_age()}\n"
      f"phone number: {employee2.display_phone_number()}\nsalary: {employee2.display_salary()}\nsalary_raise: {employee2.display_salary_raise()}")

# Object Creation and Function Call/Invocation
# When we create an object of our class, we can then pass in the values that we specified in our init method. So we can leave off "self"
# The values must be passed in the order we specified in the init method.



