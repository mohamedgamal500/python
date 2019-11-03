# fileref = open("path","operation") object from class open
fileref = open("olympics.txt", "r")

# for line in fileref:
# print(line.strip())

lines = fileref.readlines()
for line in lines[:4]:
    print(line.strip())

fileref.close()
