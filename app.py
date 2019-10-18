import math
x = input("X:")
# Type Conversions
y = int(x)+1
# str(x) , bool(x) = false if x ={"", 0 , [],none} else = true
print(y)
print("heloo \njames")
print(''' h
h
g ''')
# Mutable and Immutable Types
x = [1, 2, 3]
print(len(x))
print(x)
print(id(x))
print(id(x[0]))
print(x[0])
print(x[0:2])
print(x[:])
x.append(4)
print(x)
print(id(x))
print(id(x[0]))
y = 4
print(y)
print(id(y))
y = y+1
print(y)
print(id(y))
# Formatted Strings
first = "ahmed"
second = "jemy"
full_name = f"{first} {second}"
print(full_name)
print(type(full_name))
# Useful String Methods
course = " jemyyy"
print(course.upper())
print(course.lower())
print(course.title())

print(course.strip())  # remove whitespace

print(course.find("jem"))  # return the index of array
print(course.replace("j", "m"))

print("jemyyy" in course)
print("jemyyy" not in course)

# Numbers
y = 10
x = 0b01
print(x)
print(bin(y))
y = 15
x = 0x12c
print(x)
print(hex(y))

# Arithmetic Operators
x = 10 / 3
print(x)
x = 10 // 3
print(x)
x = 10 % 3
print(x)
x = 10 ** 3
print(x)
x = x+1
x += 1  # you can change + by any Arithmetic Operators
# hint : there is no x++ or x--

# Working with Numbers
# hint : there is no cont in python
# for more search python 3 built-in functions
# for more search python 3 math module

PI = -3.14
print(round(PI))
print(abs(PI))
print(math.floor(PI))
