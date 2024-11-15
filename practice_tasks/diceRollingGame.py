import random

posititiveAnswer = "y"
negativeAnswer = "n"
user_rolled_dice = 0

user_input = input("Roll the dice? (y/n): ").lower()

while user_input != negativeAnswer:
    if user_input != posititiveAnswer:
        print("Invalid choice!")
    
    else: 
        user_rolled_dice += 1
        user_input_dice_number = int(input("How many dice would you like to roll? (print in number format): "))
        for diceNumber in range(1, user_input_dice_number + 1):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            print(f"Dice № {diceNumber} ({x}, {y})")
           

    print("Roll the dice? (y/n): ")
    user_input = input().lower()

print("Thanks for playing!")
print(f"Total number of dice rolled: {user_rolled_dice}")


