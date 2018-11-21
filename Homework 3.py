#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:54:40 2018

@author: MariusD
"""

#White belt

class Student:
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master

Marius = Student("Marius", "Diedrich", "24", "MDBI")

print(Marius.name,Marius.last_name,Marius.age,Marius.master)


#Blue belt

entire_class = [Student("Edem", "Francois", "28", "MCSBT"),
                Student("Hannah", "Oldorf", "23", "MCBT"),
                Student("Laura", "Kageneck", "23", "MCSBT"),
                Student("Natalie", "Cedeno", "26", "MDBI"),
                Student("Tancredi", "Bernard", "21", "MCSBT"),
                Student("David", "Barrero Gonzalez", "31", "MCSBT"),
                Student("Anastasia", "Lasunina", "25", "MDBI"),
                Student("Agata", "Kaczmarek", "31","MDBI")
                ]
#add rest of class if necessary

class Student:
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master

def print_student(self):
        print(self.name + " " + self.lastname + "is a" + str(self.age) + "old student of the" + self.master + "program")

def entire_class_print(list):
    for entire_class in list:
        entire_class.print_student()