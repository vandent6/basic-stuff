import random

def generate_number():
    return random.randrange(1000,9999)


def game_runner():
    num = generate_number()
    guesses = 1
    guess = input("Iniital Guess?  ")
    print(cows_and_bulls(num, guess))
    playing = True
    while playing:
        guess = input("Guess Again  ")
        print(cows_and_bulls(num, guess))
        guesses += 1
        if str(num) == str(guess):
            playing = False

    print("Number of Guesses!  " + str(guesses))


def cows_and_bulls(num, guess):
    cows = 0
    bulls = 0
    for i in range(0,4):
        if str(guess)[i] == str(num)[i]:
            cows += 1

    bulls = 4 - cows

    return str(cows) + " cows, " + str(bulls) + " bulls"
        


game_runner()
