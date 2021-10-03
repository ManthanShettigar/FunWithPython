CORRECTANSWER = 23
print('Welcome to the number Guessing game')
print("I'm thinking of a number 1-100")

def level():
    """
    Accept the guess from the user 
    """
    choice = input('Enter your difficulty level : "easy" or "hard": ')
    if choice=='easy':
        attempts=10
        return attempts
    elif choice=='hard':
        attempts=5
        return attempts
user_attempt = level()

def guess():
    """accept guess from the user"""
    print(f"You have {user_attempt} attempts remaining to guess the number")
    user_guess=int(input('Make a guess ! : '))
    if user_guess==CORRECTANSWER:
        print('You have guessed it right !')
        exit(0)
    elif user_guess>CORRECTANSWER:
        print('Too High')
    else:
        print('Too low')



while(user_attempt!=0):
    guess()
    user_attempt=user_attempt-1
    if user_attempt==0:
        print('Sorry ! next time')