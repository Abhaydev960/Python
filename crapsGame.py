
import random

def roll_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(f"You rolled {a} + {b} = {a+b}")
    return a + b

print("----- CRAPS GAME -----")
point = roll_dice()

if point in (7, 11):
    print("You win!")
elif point in (2, 3, 12):
    print("You lose!")
else:
    print("Point is", point)
    while True:
        print("Roll again...")
        result = roll_dice()
        if result == point:
            print("You made the point. You win!")
            break
        elif result == 7:
            print("Seven-out. You lose!")
            break
