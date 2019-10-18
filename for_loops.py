# for_loops we can iterate over any object is iterable
# for x in "python": # how it works? it checks every object in the list till finish it
#     print(x)

# for x in [1, 2, 3, 4]:
#     print(x)

# for x in range(5): # x = 0,1,2,3.4
#     print(x)

# for x in range(2,5): # x = 2,3,4
#     print(x)

for x in range(0, 10, 2):  # range(start,end,step)
    print(x)

# For..Else
names = ["AJemy", "Ahmed"]
found = False
for name in names:  # it accesses every object in array and put it in variable called name
    if name.startswith("J"):
        print(name)
        found = True
        break  # when you found the name go out from iteration

if not found:  # if (found==false)
    print("Not found")
# other syntax
names = ["AJemy", "Ahmed"]
for name in names:
    if name.startswith("J"):
        print(name)
        break
else:
    print("Not found")
