import random

print("Welcome to the number guess game \n")
dificulty = int(input("Choice your dificulty(1-3): "))

if dificulty == 1:
    number = random.randint(1, 10)
elif dificulty == 2:
    number = random.randint(1, 100)
elif dificulty == 3:
    number = random.randint(1, 1000) 
else:
    dificulty = int(input("Choice a valid number: "))

def game():
    player_number = int(input("Make you choice: "))

    if player_number == number:
        print("You Win!")
    elif player_number > number:
        print("More lower!")
        game()
    elif player_number < number:
        print("More Higher!")
        game()

game()