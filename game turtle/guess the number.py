import random

x = random.randint(1, 20)
print("i thought of a number from 1 to 20")

while True:
    guess = int(input("input number: "))

    if guess < x:
        print("your number is smaler than needed")

    elif guess > x:
            print("your number is biger than neded")

    else:
            print("congrats you got the number")
            break