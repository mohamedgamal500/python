### MADE BY JEMMY ###


def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        print("FIZZBUZZ")
    elif input % 3 == 0:
        print("FIZZ")
    elif input % 5 == 0:
        print("BUZZ")
    else:
        print(input)


Input = int(input("please put your number :"))
fizz_buzz(Input)


# def fizz_buzz(input):
#     divisibleb_by_3 = input % 3
#     divisibleb_by_5 = input % 5
#     if not divisibleb_by_3:
#         return"FIZZ"
#     elif not divisibleb_by_5:
#         return"BUZZ"
#     else:
#         return input


# print(fizz_buzz(7))
