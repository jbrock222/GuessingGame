'''
Joshua Brock
CIS261
Lab 1 - Guessing Game
'''
import random

game_On = True
guessing = False
count = 1
number = 0
def heading():
    print("Guess the Number!")
    
def guess(player_guess, number):
    global count
    global game_On
    global guessing
    if player_guess < number:
        print("Too low.")
        count = count + 1
        playGame()
    elif player_guess > number:
        print("Too high")
        count = count + 1
        playGame()
    else:
        print("You guessed it in " + str(count) + " tries.")
        game_On = False
        guessing = False
        count =1
        endGame()
    
def playGame():
    global guessing
    global number
    if guessing == False:
        limit = input("Enter the limit: ")
        print("I'm thinking of a number from 1 to " + str(limit))
        number = random.randint(1, int(limit))
        guessing = True
        player_guess = int(input("Your Guess: "))
        guess(player_guess, number)
    else:
        player_guess = int(input("Your Guess: "))
        guess(player_guess, number)
    
def endGame():
    global game_On
    answer = input("Would you like to play again? (y/n) ")
    if answer == "y":
        game_On = True
        start()
    elif answer == "n":
        exit()
    else:
        print("Please enter a valid selection")

def start():
    if game_On == True:
        playGame()
    else:
        endGame()
 
heading()
start()
    


