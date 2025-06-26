import random

print("Welcome to Snake, Water , Gun Game!")
options = ['snake', 'water', 'gun']

user_score = 0
computer_score = 0
tia = 0

for i in range(1,6):
    print(f"Round {i}")

    computer = random.choice(options)
    user = input("Choose one Snake, Water, Gun : ").lower()

    if user not in options:
        print("Invalid choice!, Skip the round.\n")
        continue
    else:    
        print("You Chose:", user)
        print("Computer Chose:",computer)

        if computer == user:
            print("It's a Tia!\n")
            tia += 1
        elif (user == 'snake'and computer == 'water') or (user == 'water'and computer == 'gun') or (user == 'gun'and computer == 'snake'):
            print("You Win!\n")
            user_score += 1
        else:
            print("You Lose!\n")
            computer_score += 1

print(f'Your Score : {user_score}\nComputer Score : {computer_score}\nTia : {tia}')
if user_score > computer_score:
    print("You win!")
else:
    print("Computer win!")