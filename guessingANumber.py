import random 
secretNumber=random.randint(1,50)
print("I am thinking a number between 1 to 50")
print("\nyou have 6 chances to guess the number")
for guessNumber in range(1,7):
    guess=int(input("Take a guess"))
    if guess>secretNumber:
        print("Your guess is too high")
    elif guess<secretNumber:
        print("your guess is too low")
    else:
        break
if guess==secretNumber:
    print("Good job! you guessed my number in "+str(guessNumber)+"guesses")
else:
    print("the number I was thinking is "+str(secretNumber)) 