# Lecture - 6  Strings

# String is data type that stores a sequence of characters.

# Basic Operation 
# Concatenation 

# Id Card

first_name = "Piyush"
last_name = "Bhatt"

full_name = first_name + " " + last_name

# print(full_name)
# len --> length of any string
# print(len(full_name))


# Indexing
# It is used to access single word from a big word or sentence.

state_name = "Uttrakhand"
# index is start from 0 to max. 
# print(len(state_name)) # 10
# print(state_name[7])   

# Slicing
# It is used to access multiple word from a big word or sentence.
# Slicing is used to get a substring from a string.

# Slicing is done by using [start:end:step]  ending idx is not included

# slice_state_name = state_name[5:10] # 5 to 9
# print(slice_state_name)

# Slicing 
# negative index is used to access the string from the end of the string.

# fruit = "Apple"
# print(fruit[-4:-1]) # ppl

# String Function 

# link - https://www.w3schools.com/python/python_ref_string.asp

# Practice - 1

# WAP to input user's first name & print its length

input_name = input("Please Enter your name : ")
print(len(input_name))