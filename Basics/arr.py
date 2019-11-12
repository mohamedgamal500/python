from array import *
vals = array('i', [1, 3, 4])
print(vals)
# initializing array with array values
# initializes array with signed integers
arr = array('i', [1, 2, 3, 1, 5])
print(type(arr))
# printing original array
print("The new created array is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")
# using pop() to remove element at 2nd position
print("The popped element is : ", end="")
print(arr.pop(2))

# printing array after popping
print("The array after popping is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")
