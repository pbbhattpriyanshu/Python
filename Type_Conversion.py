# Lecture - 5  Type conversion and type casting

# The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion: Implicit and Explicit.

# Type Conversion - automatic conversion which done by compiler. if its possible to convert then only. like - int(2) convert into float(2.0).

a = 23   # int
b = 21.34  # float

sum = a + b   # float

# print(type(a))
# print(type(b))
# print(type(sum))

# print(sum)

# error 

c = "32" # string
d = 65   # int 

# sum = c + d

# print(type(c))
# print(type(d))

# print(sum)
# Upper Error --> Solve = Type Casting

# Type Casting - manual conversion which done by user. Which is forcefuly done by user, in this case maybe possible of data damage.  like - int(2.0) convert into int(2).

e = int(c) # string to int

sum = e + d

print(type(e))
print(type(d))
print(type(sum))
print(sum)