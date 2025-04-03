# Datatypes & Keywords

# A data type is a classification that specifies which type of value a variable can hold. In Python, there are several built-in data types that can be used to store different types of values. The most commonly used data types in Python are:

# integer
# float
# list
# string
# boolean
# tuple
# set
# dictionary
# NoneType 

#Each of these data types has its own characteristics and uses.

#
# 1. Integer: An integer is a whole number, positive or negative, without decimals. In Python, integers can be of any length. For example: 

marks = 92
age = 20

print(marks )  # Output: 92
print(age)  # Output: 20
print(type(marks))  # Output: <class 'int'>

# 2. Float: A float is a number that has a decimal point. In Python, floats can also be of any length. For example:

average = 43.31

print(average)  # Output: 43.31
print(type(average))  # Output: <class 'float'>

# 3. String: A string is a sequence of characters enclosed in quotes (single or double). Strings can contain letters, numbers, and special characters. For example:

name = "Piyush bhatt"
address = 'Gujarat, India'
print(name)
print(address)
print(type(address))  # Output: <class 'str'>

# 4. Boolean: A boolean is a data type that can have one of two values: True or False. Booleans are often used in conditional statements and logical operations. For example:

is_student = True
is_employed = False
print(is_student)  # Output: True
print(is_employed)  # Output: False
print(type(is_student))  # Output: <class 'bool'>

# 5. List: A list is a collection of items that can be of different data types. Lists are mutable, meaning that their contents can be changed after they are created. Lists are defined using square brackets []. For example:

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(type(fruits))  # Output: <class 'list'>

# Optional

# 6. Tuple: A tuple is similar to a list, but it is immutable, meaning that its contents cannot be changed after it is created. Tuples are defined using parentheses ().

# 7. Set: A set is an unordered collection of unique items. Sets are mutable, but they do not allow duplicate values. Sets are defined using curly braces {} or the set() function.

# 8. Dictionary: A dictionary is a collection of key-value pairs. Dictionaries are mutable and are defined using curly braces {} with key-value pairs separated by colons (:).

# Keyword
# Keywords are reserved words in Python that have special meanings and cannot be used as variable names. They are used to define the syntax and structure of the Python programming language.

# Print Sum 

a = 43
b = 35

sum = a + b
print(sum)  # Output: 78

