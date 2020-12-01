import random
from termcolor import colored
#pip install termcolor

print('Welcome to the Number Guess game\nHope U will have lots of FUN!!!')

random_number = random.randint(0,100)
win, intial_turns =False, 1

print("Tell me in how many terms you can guess the number\n")
turns = input()

while win == False and intial_turns <= int(turns):
    intial_turns += 1
    your_number = input("Enter a number between 0 to 99\n")
    if your_number == random_number:
        print(colored('You WON! Congratulations on guessing the CORRECT NUMBER\n','blue'))
        win = True
        
    else:
        print('You guessed the WRONG NUMBER!  Keep trying')
        if int(your_number) > random_number:
            print(colored("Your number is a bit higher,try guessing a smaller number\n",'red'))
        else:
            print(colored("Your number is bit lower,try guessing a higher number\n",'red'))

    if intial_turns == turns:
        print(colored('Sorry!! Your out of turns!! Try again next time!','red'))
print(colored('Sorry!! Your out of turns!! Try again next time!\n','red'))
print(colored(f'The random number is {random_number}','yellow'))
