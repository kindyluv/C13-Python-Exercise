"""
 Creating a Simple Employee Class
    Let's say we are building an application for a company and we want to represent the employees in our python code
    We are going to create a class for the employees.
    The employee class should have:
    instance variables such as firstname, lastname, email, and salary.
    class variables such as annual_raise_salary, number_of_employees
    methods such as method to display employees fullname, email, and salary, and also methods to raise the employees salaries by a certain percentage and
    methods to increase the number of employees.
"""


class Employee:

    salary_raise_amount = 1.04
    number_of_employees = 0

        Employee.number_of_employees += 1

# this increases the number of employees by 1 each time we create a new employee. For this case, it doesn't make sense to use self.number_of_employees because with the raises it's nice to have that constant class value that can be overridden per instance.


    def display_full_name(self):
        return f"full name : {self.firstname} {self.lastname}"
    def display_salary(self):
        return self.salary
    def display_email(self):
        return self.email
    def display_age(self):
        return self.age
    def apply_salary_raise(self):
        self.salary = int(self.salary * self.salary_raise_amount)
        return self.salary

    """
    You can access the class variable annual_salary_raise 
    1. through the class itself using:  Employee.annual_salary_raise
    2. through the instance using: self.annual_salary_raise 
    
    It is better to use self.annual_salary_raise instead of Employee.annual_salary_raise because that will give us the ability 
    to change the annual_salary raise for a single instance if we really wanted to.
    Also using self here will allow any subclass to override that constant if they wanted to.
    
    """
# Creating a class method
    @classmethod
    def set_salary_raise_amount(cls, amount):
        cls.salary_raise_amount = amount

# using a class method as an alternative constructor:
    @classmethod
    def from_string(cls, employee_str):
        firstname, lastname, salary = employee_str.split("-")
        return cls(firstname, lastname, salary)

"""
    Creating A Static Method:
    let's say that we want a simple function that would 
    take in a day and return whether or not the day falls on a weekday.
    So that has a logical connection to our employee class but it doesn't actually 
    depend on any specific instance or class variable.So you'll make this a static method
"""

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True





# Employee Class  Test

print(Employee.number_of_employees)
# it returns 0 because at this point no employee has been created.

# Object Creation
employee1 = Employee("Jude", "Onyedeke", 19, 500000)
employee2 = Employee("Ekpei", "Raphael", 25, 100000)

# Another way of creating objects via class methods
employee_str_1 = "John-Doe-70000"
employee_str_2 = "Steve-Smith-30000"
employee_str_3 = "Jane_Doe-90000"

new_employee_1 = Employee.from_string(employee_str_1)
print(new_employee_1.email)
print(new_employee_1.salary)

# Calling class method
Employee.set_salary_raise_amount(1
# You can run the class method from the instance as well, but it doesn't make much sense and hence should be avoided.
# employee1.set_raise_amount(1.05)

print(Employee.number_of_employees)
# it returns 2 because it was incremented twice when we instantiated both of our employees.


# 1. Instance Method call - Way 1
print(employee1.display_full_name())
print(employee1.display_salary())
print(employee1.display_email())
print(employee1.apply_salary_raise())

print(employee2.display_full_name())
print(employee2.display_salary())
print(employee2.display_email())
print(employee2.apply_salary_raise())



# 2. Instance Method call - Way 2:

print(Employee.display_full_name(employee1))
print(Employee.display_salary(employee1))
print(Employee.apply_salary_raise(employee1))

print(Employee.display_full_name(employee2))
print(Employee.display_salary(employee2))
print(Employee.apply_salary_raise(employee2))

print(Employee.salary_raise_amount)
print(employee1.salary_raise_amount)
print(employee2.salary_raise_amount)

print(Employee.number_of_employees)


"""
 Some class variables can be overridden or changed for a single instance if need be.
 for example, annual_salary_raise can be changed for an employee. 
 
 There is no use case where i can think of where we would want the total number of employee to be different for any one instance.
"""

employee1.salary_raise_amount = 2.05
print(employee1.salary_raise_amount)
print(employee1.salary)

# namespace of employee1
print(employee1.__dict__)

# namespace of employee2
print(employee1.__dict__)

"""
To confirm if our static method is working:
1. import datetime module
2. create a new date

"""

# Calling static method
import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))




