#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:15:52 2020

@author: sindy
"""

class Student:
    def __init__(self, name, lastname, year_scholarship, school):
        self.name = name
        self.lastname = lastname
        self.school = school
        self.year_scholarship = year_scholarship        
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def month_scholarship(self):
        return self.year_scholarship / 12.0


anna = Student("Anna", "Perez", 12000, "Oxford")

"""
Imagine you’ve got a class like the above, and you want to create a similar 
class with some extra functionality. For example, a student that not only has 
marks but also a salary—a `WorkingStudent`:
"""

#class WorkingStudent:
#    def __init__(self, name, lastname, school, salary):
#        self.name = name
#        self.school = school
#        self.marks = []
#        self.salary = salary
#
#    def average(self):
#        return sum(self.marks) / len(self.marks)
#
#
#    def weekly_salary(self):
#        return self.salary *37.5

#rolf = WorkingStudent("Rolf", "MIT", 15.50)
#rolf.marks.append(57)
#rolf.marks.append(99)
#print(rolf.average())
#print(rolf.weekly_salary())
"""
However you can see there’s a lot of duplication between our `Student` and 
`WorkingStudent` classes. Instead, we may choose to make our `WorkingStudent` 
extend the `Student`. It keeps all the same functionality, but we can add more.
"""

class WorkingStudent(Student):
    def __init__(self, name, lastname, year_scholarship, school, salary):
        super().__init__(name, lastname, year_scholarship, school)
        self.salary = salary
        
    @property   
    def weekly_salary(self):
       return self.salary *37.5

rolf = WorkingStudent("Rolf", "Wolf", 14000, "MIT", 15.50)
anne = WorkingStudent("Anne", "Rice", 8000, "MIT", 17.50)


rolf.marks.append(57)
rolf.marks.append(99)
anne.marks.append(85)
anne.marks.append(72)

print(rolf.month_scholarship())
print(rolf.average())
print(rolf.weekly_salary)