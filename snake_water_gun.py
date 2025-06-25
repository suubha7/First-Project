import random

print("Welcome to Snake, Water , Gun Game!")
options = ['snake', 'water', 'gun']

computer = random.choice(options)
user = input("Choose one Snake, Water, Gun : ").lower()

if user not in options:
    print("Invalid choice !")

else:    
    print("\nYou Chose:", user)
    print("Computer Chose:",computer)

    if computer == user:
        print("It's a Tia!")

    elif (user == 'snake'and computer == 'water') or (user == 'water'and computer == 'gun') or (user == 'gun'and computer == 'snake'):
        print("You Win!")

    else:
        print("You Lose!")

