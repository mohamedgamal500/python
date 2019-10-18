# def funcname(parameter_list):
#     pass


def increment(number, by):  # by=1 increment by one then call increment(5) out>(5,6)
    return(number, number+by)


out = increment(5, 7)
print(out)

# type of


def decrement(number: int, by: int = -1) -> tuple:
    return(number, number+by)  # to retun more than one args we use tuple


out = decrement(5)
print(out)

# args

# tuple


def miltiply(*list):
    total = 1
    for number in list:
        total *= number
    return total

# list
# print(miltiply(5, 5, 10))
# def miltiply(list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(miltiply([5, 5, 10]))

# **args args with key
def save(**user):
    print(user)
    print(user["id"])
    print(user["name"])


save(id=1, name="jemy")

# scope
# every local variable dont have block level scope

# local


def greet():
    if True:
        message = "j"

    print(message)  # out of block level of if but it can read it


greet()

# global
hint = "b"


def welcome():
    hint = "a"
    print(hint)
    # global hint # dont use it....it will affect
    # hint = "g"


welcome()
print(hint)
