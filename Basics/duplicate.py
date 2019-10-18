numbers = [1, 2, 2, 3, 3, 4, 5, 5, 6]
req_list = []
for num in numbers:
    if num not in req_list:
        req_list.append(num)

print(req_list)
