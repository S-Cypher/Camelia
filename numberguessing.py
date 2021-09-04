#Number guessing game
#Keira Stewart

#imported libraries
import random
import os
from time import sleep

#misc variables
os.system('cls') #clears the terminal
game = "start" #used for the while loop
times = 0 #extra for the player

number = random.randrange(1,101)
print("Number Guessing Game!")
sleep(1)
print("I'm thinking of a number between 1 and 100")
sleep(1)
print("Try to guess it!")
guess = int(input("Answer:"))

while game !="end":
    if guess < number:
        times +=1
        print("Try to guess higher")
        guess = int(input("Answer:"))

    elif guess > number:
        times +=1
        print("Try to guess lower")
        guess = int(input("Answer:"))

    elif guess == number:
        print("You guessed my number!")
        sleep(1.3)
        print("It took you", times, "guesses")
        sleep(1.3)
        print("Congrats!")
        game="end"
