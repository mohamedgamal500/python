text = "bat cat mat cat bat cat"
words = text.split()
print(words)

d = dict()
print(d)
for word in words:
    if word in d:
        d[word] = d[word]+1
    else:
        d[word] = 1
lol = d.values()
print(lol)
print(type(lol))
descend = list(d.values())
descend.sort(reverse=True)
print(descend)


list_tuples = [('cat', 3), ('hat', 4), ('mat', 2)]
list_tuples.sort(reverse=True)
print(list_tuples)


def add(x):
    return x+1


fun = add(5)
print(fun)


def inc(x): return x+1


print(inc(7))

'''inc=lambda x : x+1

print(inc(7))'''


people = {'c': 1, 'better': 2, 'betty': 1, 'a': 1}
print(type(people))
print(people)
p = list(people.items())
print(type(p))
print(p)
p_s = sorted(p, key=lambda t: t[0])
print(p_s)

p_sortna = sorted(p_s, key=lambda t: t[1], reverse=True)
print(p_sortna)
res = p_sortna[:3]
print(res)

p_sr = sorted(people, key=lambda t: t[0])
print(p_sr)

'''list_tuples = []
# Print the contents of dictionary (dictionary keys >> list)
for key in list(d.keys()):
    x = (key, d[key])
    list_tuples.append(x)
    print(x)

list_tuples.sort(reverse=True)
print(list_tuples)'''
