print('solution1')
numbers = [5, 2, 5, 2, 2]
for num in numbers:
    for dr in range(num):
        print('x', end="")
    print('')
# other solution
print('solution2')
numbers2 = [5, 2, 5, 2, 2]
for num2 in numbers2:
    count = ''
    for dr in range(num2):
        count += 'x'
    print(count)
# other solution
print('solution3')
numbers3 = [5, 2, 5, 2, 2]
for num3 in numbers3:
    print('x'*num3)
