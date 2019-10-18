# and , or , not

# not
name = " "
if not name.strip():  # it means if name is emty string
                      # strip removes whitespace
    print("name is empty")

# and
age = 22
if age >= 18 and age < 65:  # we can write also 18 <= age < 65
    print("acceptable")
# Ternary Operators
height = 170
if height >= 170:
    message = "Eligible"
else:
    message = "Not Eligible"
# like in C >
#  message = height >= 170 ? "Eligible" : "Not Eligible"

# in Python >
#message = "Eligible" if height >= 170 else "Not eligible"

print(message)
