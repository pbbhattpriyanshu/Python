# Lecture 1 - Variables

# A variable is a name given to a memory location in a program. It is used to store data that can be changed during the execution of the program. Variables are used to hold values that can be referenced and manipulated in a program. In Python, variables are created when a value is assigned to them using the assignment operator `=`.

name = "Piyush bhatt"
age = 20
cgpa = 9.0
is_student = True

print ("My name is : ", name)  # Output: Piyush bhatt
print ("My age is : ", age)  # Output: 20
print ("My cgpa is : ", cgpa)  # Output: 9.0
print ("Is student : ", is_student)  # Output: True

# The above code creates four variables: name, age, cgpa, and is_student. The values of these variables are printed using the print() function.

# The variables can be changed during the execution of the program. For example, we can change the value of the age variable as follows:

age = 21
print ("My new age is : ", age)  # Output: 21

# In the above code, the value of the age variable is changed from 20 to 21. The new value is printed using the print() function. 

print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'int'> 
print(type(cgpa))  # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>

# The type() function is used to get the type of a variable. In the above code, the type of each variable is printed using the print() function. The output shows that name is a string, age is an integer, cgpa is a float, and is_student is a boolean.
# The type of a variable is determined by the value assigned to it. In Python, variables are dynamically typed, which means that the type of a variable can change during the execution of the program.

