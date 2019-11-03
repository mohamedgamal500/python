'''same as fileobj = open('jemy.txt','r') as fileobj 
    and you dont need to use close file'''
with open('jemy.txt', 'r') as fileobj:
        lines = fileobj.readlines()
        for line in lines[:]:
            print(line.strip())
