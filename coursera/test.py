x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
print(x)
print(y)
# y += ['sheep'] #same object
y = y + ['sheep']  # different object
print(y)
print(x)
