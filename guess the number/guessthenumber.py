import random
CORRECTANSWER = random.randint(1,100)
print(
    ''''  __ _ _   _  ___  ___ ___ 
 / _` | | | |/ _ \/ __/ __|
| (_| | |_| |  __/\__ \__ \.
 \__, |\__,_|\___||___/___/
  __/ |                    
 |___/ '''''
)
print('Welcome to the number Guessing game')
player_name = input("Hello, What's your name?")

print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')
print('\n10 chances in Easy game, 8 in medium and 5 in Hard game.')

def level():
    """
    Accept the guess from the user 
    """
    choice = input('Enter your difficulty level : "type E or e or easy for Easy level" , "type M or m or medium for Medium level " or "type H or h or hard For Hard level": ')
    if choice=='easy'or choice == 'e' or choice == 'E':
        attempts=10
        return attempts
    elif choice=='medium' or choice == 'm' or choice == 'M':
        attempts=8
        return attempts
    elif choice=='hard'or choice == 'h' or choice == 'H':
        attempts=5
        return attempts
user_attempt = level()

def guess():
    """accept guess from the user"""
    print(f"You have {user_attempt} attempts remaining to guess the number")
    user_guess=int(input('Make a guess ! : '))
    if user_guess==CORRECTANSWER:
        print('You guessed the number in ' + str(user_attempt) + ' attempts!')
        exit(0)
    elif user_guess>CORRECTANSWER:
        print('Too High')
    else:
        print('Too low')



while(user_attempt!=0):
    guess()
    user_attempt=user_attempt-1
    if user_attempt==0:
        print('You did not guess the number, The number was ' + str(CORRECTANSWER))
        print('Sorry ! next time')