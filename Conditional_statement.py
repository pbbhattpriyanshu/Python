# Lecture 7 - Conditional Statement
# Conditional statements are used to perform different actions based on different conditions.
# In Python, the most common conditional statements are `if`, `elif`, and `else`. These statements allow you to execute different blocks of code based on the evaluation of a condition.

# The `if` statement is used to test a condition. If the condition is true, the block of code inside the `if` statement is executed. If the condition is false, the block of code inside the `if` statement is skipped.
#
# The `elif` statement is used to test multiple conditions. If the first condition is false, the program checks the next condition. If that condition is true, the block of code inside the `elif` statement is executed. If all conditions are false, the block of code inside the `else` statement is executed.

# The `else` statement is used to execute a block of code if all previous conditions are false. It is optional and can be omitted if not needed.
# The syntax for the `if`, `elif`, and `else` statements is as follows:

# Grade System

# marks = int(input("Enter your marks: "))

# if marks >= 85:
#     print("Grade: A")
# elif marks >= 70 and marks < 85:
#     print("Grade: B")
# elif marks >= 50 and marks < 70:
#     print("Grade: C")
# else :
#     print("Grade: D")


# # In the above code, the program takes input from the user for marks and checks the conditions to determine the grade. The program prints the grade based on the marks entered by the user.

# Traffic Light System
# color = red (stop), yellow (slow down), green (go), different colors (light is broken)

# color = input("Enter the color of the traffic light (red, yellow, green or any other color): ")

# if color == "red":
#     print("Stop!")
# elif color == "yellow":
#     print("Slow down!")
# elif color == "green":
#     print("Go!")
# else: 
#     print("The traffic light is broken!")

# In the above code, the program takes input from the user for the color of the traffic light and checks the conditions to determine the action to be taken. The program prints the action based on the color entered by the user.

# Age Verification System

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are not eligible to vote.")
# elif age >= 18 and age < 60:
#     print("You are eligible to vote.")    
# else:
#     print("You are a senior citizen and eligible to vote.")

# In the above code, the program takes input from the user for age and checks the conditions to determine the eligibility to vote. The program prints the eligibility based on the age entered by the user.

# Practice Problem

# A = 5 , G = M
# A = 2 , G = F

# A = int(input("Enter the value of A: "))
# G = (input("Enter the value of G: "))

# if (A == 1 or A == 2) and G == "M":
#     print("Fee is 100")
# elif(A == 3 or A == 4) or G == "F":
#     print("Fee is 200")
# elif(A == 5 and G == "M"):
#     print("Fee is 300")
# else:
#     print("No fee")

# In the above code, the program takes input from the user for A and G and checks the conditions to determine the fee. The program prints the fee based on the values entered by the user.

# Operator table

# AND 
# true and true = true
# true and false = false
# false and true = false
# false and false = false

# OR
# true or true = true
# true or false = true
# false or true = true
# false or false = false

# Calculate Simple Interest

# P = Principal amount
# R = Rate of interest
# T = Time in years
# SI = Simple Interest
# SI = (P * R * T) / 100

# P = float(input("Enter the principal amount: "))
# R = float(input("Enter the rate of interest: "))
# T = float(input("Enter the time in years: "))

# SI = (P * R * T) / 100

# print("The simple interest is: ", SI)

# In the above code, the program takes input from the user for principal amount, rate of interest, and time in years and calculates the simple interest using the formula. The program prints the simple interest based on the values entered by the user.

# Comments 

# Single line comment

"""
This is a Multi line comment
lorem ipsum dolor sit amet, consectetur adipiscing elit.
"""

# Practice question

# WAP to check if a number entered by the user is odd or even

# User Input
# num = int(input("Enter the number: "))

# # check the number is even or odd
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("Number is odd")

# WAP to find greatest of 3 numbers entered by user.

# Input by user
a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

# Check the greatest number among
if a > b and a > c:
    greatest = a
elif b > a and b > c:
   greatest = b
else:
    greatest = c

print(f"The Greatest Number is {greatest}")