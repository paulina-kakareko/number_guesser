import random

random_number = random.randint(1, 20)



lista = []
your_guess = input("Guess a number from range (1,20): ")
if your_guess.isdigit():
    your_guess = int(your_guess)
    if your_guess > random_number:
        print("You are above the number.")
    elif your_guess < random_number:
        print("You are below the number.")
else:
    print("This is not a number!")



lista.append(your_guess)


while your_guess != random_number:
    your_guess = input("Try once again! Guess a number from range (1,20): ")
    if your_guess.isdigit():
        your_guess = int(your_guess)
        if your_guess > random_number:
            print("You are above the number.")
        elif your_guess < random_number:
            print("You are below the number.")
    else:
        print("This is not a number!")
    lista.append(your_guess)

print(f"You got it in {(len(lista))} guesses!")


