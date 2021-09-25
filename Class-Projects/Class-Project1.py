#
# Python: 3.9.5
#
# Author: Randall Jackson
#
#
# Purpose: Creating parent and child classes.
# Child classes take attributes from the parent classes. 
# 
#

class User:
    #Defines the attributes of the class
    name = 'Randy Jackson'
    email = 'Randalljackson20@gmail.com'
    password = 'Topsecret'
    account_number = 1

class Student(User):
    #Has all attributes of User + Tuition cost and Course
    Tuition_cost = '$1m'
    Course = 'Python Course'

class Employee(User):
    # Has attributes of User but not Student
    Salary = '$800/h'
    Job = 'Do nothing'

print("User's Name: {}\nEmail: {}\nPassword: {}\nAccount Number: {}".format(User.name, User.email, User.password,User.account_number))
# Even though a name was never defined in the child class "Student", it will 
# still print the name from the class "User" since that is the Parent Class
print("\nThe student {} has a totally fair tuition cost of {}.\nHe is taking the {}!".format(Student.name,Student.Tuition_cost,Student.Course))
print("The employee {} makes {} with the worlds easiest job role: {}!".format(Employee.name,Employee.Salary,Employee.Job))
