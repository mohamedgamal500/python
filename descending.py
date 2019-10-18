numbers = [1, 2, 4, 7, 6, 8, 99, 88, 22]
print(type(numbers))
numbers.sort(reverse=True)
print(numbers)
d = {'name': 'jemy',
     'age': '21'
     }

print(d.items())

copy = dict(d)

copy.pop('age')

print(d.items())
print(copy.items())
