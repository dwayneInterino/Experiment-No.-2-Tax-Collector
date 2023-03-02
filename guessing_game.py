import random
print("You have 10 chances in order to guess the correct number from 1-20.")
loopCount = 0
randomNumber = random.randint(1, 20)
while loopCount != 10:
    loopCount = loopCount + 1
    guess = int(input("Please input your guess {0}:  ".format(loopCount)))
    if guess == randomNumber:
        print("Correct Guess!")
        print("Your number of guesses is {0}".format(loopCount))
        break
    elif guess > 20:
        print("Too high! Please retry this guess!")
        loopCount = loopCount - 1
    elif guess < 1:
        print("Too low! Please retry this guess!")
        loopCount = loopCount - 1
print("The Correct Number is {0}".format(randomNumber))
