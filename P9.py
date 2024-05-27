# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly
# right.
import random
c = random.randint(1, 9)
print("In this challenge you have to guess the number!The game would not stop until you guessed the right one!")
d = 0
i=1
while d != 'no':
    user = int(input("Guess the number:"))
    if user == c:
        print("You guessed right!The number is", c, "!")
        print("You took",i,"guesses.")
        d = input("Wanna play again?")
    elif user > c:
        print("You guessed too high!")
        i+=1
    else:
        print("You guessed too low!")
        i+=1

