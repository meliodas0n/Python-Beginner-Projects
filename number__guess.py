import random


print("Hello there\n")
print("Welcome to the Number Guess game\n")
print("Hope you will have lots of FUN!!!")

random_number = random.randint(0, 1001)
win = False
intial_turns = 1

print("Tell me in how many terms you can guess the number\n")
turns = input()

while win == False and intial_turns <= int(turns):
    intial_turns += 1
    your_number = input("Enter a number between 0 to 1000\n")
    if your_number == random_number:
        print("You WON!\n")
        print("Congratulations on guessing the CORRECT NUMBER\n")
        win = True
        
    else:
        print("You guessed the WRONG NUMBER!\n")
        print("Keep trying")
        if int(your_number) > random_number:
            print("Your number is a bit higher,try guessing a smaller number\n")
        else:
            print("Your number is bit lower,try guessing a higher number\n")

    if intial_turns == turns:
        print("Sorry!! Your out of turns!!\n")
        print("Try again next time")

    print("Sorry!! Your out of turns!!\n")
    print("Try again next time\n")

