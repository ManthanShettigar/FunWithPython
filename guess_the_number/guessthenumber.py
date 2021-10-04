import random as r
import time

CORRECTANSWER = r.randint(1,100)
print('\n',20*'*', 'Welcome to GUESS THE NUMBER', 20*'*')
time.sleep(1)

print('\nThe Rules are Simple, the computer will choose a number randomly and you have to guess it.')
time.sleep(2)
print('\nYou will get number of choices based on your difficulty choice.')
time.sleep(1.5)
print('\n10 chances in Easy difficulty, 7 in medium and 5 in Hard difficulty.')
time.sleep(1.5)
print('\nAll the best. ;)')

time.sleep(1)
print("\nThinking of a number from 1-100")
time.sleep(2)


def level():
    """
    Accept the guess from the user 
    """
    choice = input('Enter your difficulty level(E for easy, M for medium and H for hard)\n')
    if choice=='E' or choice == 'e':
        attempts=10
        return attempts
    elif choice=='M' or choice == 'm':
        attempts=7
        return attempts
    elif choice=='h' or choice == 'H':
        attempts=5
        return attempts

user_attempt = level()

def guess():
    """accept guess from the user"""
    print(f"\nYou have {user_attempt} attempts emaining to guess the number")
    user_guess=int(input('Make a guess :: '))
    if user_guess==CORRECTANSWER:
        print('\nYou have guessed it right !!!')
        exit(0)
    elif user_guess > CORRECTANSWER + 15:
        if(user_attempt > 1):
            print('Your guess is too HIGH')
    elif user_guess < CORRECTANSWER - 15:
        if(user_attempt > 1):
            print('Your guess is too LOW')
    elif user_guess > CORRECTANSWER:
        if(user_attempt > 1 ):
            print('Guess a bit lower')
    else:
        if(user_attempt > 1):
            print('Guess a bit higher')



while(user_attempt!=0):
    guess()
    user_attempt=user_attempt-1
    if user_attempt==0:
        print('\nYou ran out of chances, you can try again :)')


