
class Employee:
    pass
"""
    Example of Inheritance:
    For our OOP so far, we have been working with the Employee Class.
    Let's say we wanted to get a little more specific here and create different types of employees, for example developers and managers. These are good candidates for subclasses because both developers and managers are going to
    have names, email addresses and a salary and those are all things that our employee class already has. So instead of copying all the Employee Class code into our developer and manager subclasses, we can just reuse that code by inheriting it from the Employee Class.
"""
# Here we create a new class Developer which inherits the parent Class Employee
class Developer(Employee):
    salary_raise_amount = 1.10

# Here we create two new developers and pass in their information

developer1 = Developer("Jude", "Onyedeke", 19, 50000)
developer2 = Developer("Ekpei", "Raphael", 25, 10000)

print(developer1.email)
print(developer2.email)

# print(help(Developer)) # helps us visualize inheritance
"""
    Customizing our Subclass

# We can make changes to our subclasses without about breaking anything in the parent class

1. changing the salary-raise amount of a Developer 
If we print the our current developer's salary and apply_salary_raise_amount(of 4%) and developers salary again, we would get the values inherited from the Employee class.
let's say that we want our developers to have a raise amount of 10%, we can change that inside the developer's class above and then re_run our code.
We can see that it used the developer's raise_amount instead of the instance raise_amount.
If we change the instance Developer back to an Employee instead of a Developer and then re-run this, then we can see that it's back to that employee 4% amount

The thing to take away here is by changing the raise_amount in our subclass, it didn't have any effect on our Employee instances so they still have that raise amount of 4% 

2. More complex changes

"""
print(developer1.salary)
developer1.apply.salary_raise_amount()
print(developer1.salary)
