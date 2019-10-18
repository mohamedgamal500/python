guess = int(input("Guess:"))
answer = 5
yours = True
while answer != guess:
    print("in correct")
    yours = False
    guess = int(input("Guess:"))
yours = True
if yours:
    print("correct")

# while...else
guess = int(input("Guess:"))
answer = 8
while answer != guess:
    print("in correct")
    guess = int(input("Guess:"))


else:  # after finishing the loop
    print("correct")
