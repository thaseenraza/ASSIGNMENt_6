# Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
# Each employee information consists of Name, DOB, Height, City, State. Write a python program 
# that reads this information from the JSON file and saves the information into a list of objects
# of Employee class. Finally print the list of the Employee objects.

import json


class Employee:

    def __init__(self,Name,DOB,Height,City,State):
        self.Name = Name
        self.DOB = DOB
        self.Height = Height
        self.City = City
        self.State = State

with open('D:\\New folder (2)\\OneDrive\\Desktop\\empl.json') as file:
    data = json.load(file)
    print(data)
    print(type(data))

employees = []

for emp in data['employees']:
    employees.append(Employee(emp['Name'],emp['DOB'],emp['Height'],emp['City'],emp['State']))

for emp in employees:
    print([emp.__dict__])
print(type(employees))