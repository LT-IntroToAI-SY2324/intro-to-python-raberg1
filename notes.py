# This File will be used as notes for the basics of python
# There is a lot in this file, you should add, subtract, change things as needed to help fully understand the process.
# Mr. Berg will be going over all parts, but will not be grading anything in this file

# types

# str

y: str = "I love Computer Science!"
print(y)
# numbers
mynum = 47
anothernum = 47.7
print(type(mynum))
print(type(anothernum))
print(type(y))

# bools - True, False
flag: bool = True
print(flag)
print(type(flag))

# lists - can hold a list of items of any type
lane_tech = ["chicago", "high school", 1908, 60618, "addison/western"]
# print(lane_tech.reverse())
print(lane_tech)
# z = lane_tech.pop(3)
# print(z)


# Indices
# print(lane_tech[1])
# print(lane_tech[-3])
# print(lane_tech[len(lane_tech)-1])

# Slices
print(lane_tech[1:3])
print(lane_tech[:3])
print(lane_tech[1:])
print(lane_tech[:])

# Functions

# defining a function
def hello_world():
    print("hello world")

# calling a function
hello_world()
hello_world()

def add_two(n):
    """Takes a number and returns that number + 2
    
    Args: 
        n - a number
    
    Returns:
        the input number + 2
    """
    return n + 2

assert add_two(5) == 7, "add_two with input 5 test"
assert add_two(-2) == 0, "add_two with input -2 test"
assert add_two(0) == 2, "add_two with input 0 test"

# Loops

# For Loop Template 1
# do something for each item in a list
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
for el in lst:
    print(el)

# For Loop Template 2
# do something n times
print(list(range(5)))
for i in range(5):  
    print("Intro to AI")

# For Loop Template 3
# do something for each item in a list but we care about the index
print(lst)
for r in range(len(lst)):
    if lst[r] == 'b':
        lst[r] = 'c'

print(lst)

# Dictionaries

dict = {"name": "rob", "age": 40}
print(dict)
print(dict["age"])
print(dict['name'])

# Random
import random

food = ['pizza', 'carrots', 'eggs']
dinner = random.choice(food)
print(dinner)

# f String
age = 25
# print("Mary is" , age , "years old")
print(f"Mary is {age} years old, and it is the year {mynum}")


# Here are some more notes