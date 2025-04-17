# Lecture 4 - Input 

# Always raw input is taken in the form of string, if you define data types by taking input, at that time only values store according to their datatypes .

# String input 
# name = input("name : ")
# print("My name is ",name)

# int input

# age = int(input("age : "))
# print("My age is ",age)

# float input 

# cgpa = float(input("cgpa : "))
# print("My CGPA is ",cgpa)

# Project - ID Card
# Create a simple ID card program=u74that takes user input for various fields and displays the information in a formatted manner.

student_id = [
	input("Whats your Name : "),
	input("Whats your Course : "),
	input("Whats your Domain : "),
	input("Whats your College name : "),
	input("Any Working Experience : "), 
	input("You are Student T/F : ")
]

print(student_id)