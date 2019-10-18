#numbers = [1, 2, 3, 45, 67, 88, 99, 77, 67, 890]


input_string = input("Enter a list element separated by space ")
numbers = input_string.split()
print(numbers)


def find_max(numbers):
    #ref = 0  #
    ref = int(numbers[0])
    for num in numbers:
        x = int(num)
        print(x)
        print('type(x)')
        print(type(x))
        if x > ref:
            ref = x
            print(ref)
            print('type(ref')
            print(type(ref))
    print(f'the largest number is : {ref}')


find_max(numbers)
