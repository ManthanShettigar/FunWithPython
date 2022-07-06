from pydoc import doc
import random
import time

def start_game():
    answer = random.randint(1,100)
    attempt = 1;

    while True:
        
        userAnswer = int(input("Attempt " + str(attempt) + " :"))

        if userAnswer == answer:
            print("Congratuations, you have gotten the correct number in " + str(attempt) + " tries.")
            break;
        elif userAnswer < answer - 35:
            print("Freezing")
        elif userAnswer > answer + 35:
            print("Freezing")
        elif userAnswer < answer - 20:
            print("Cold")
        elif userAnswer > answer + 20:
            print("Cold")
        elif userAnswer < answer - 10:
            print("Warm")
        elif userAnswer > answer + 10:
            print("Warm")
        elif userAnswer < answer - 5:
            print("Warmer")
        elif userAnswer > answer + 5:
            print("Warmer")
        elif userAnswer < answer:
            print("Hot")
        elif userAnswer > answer:
            print("Hot")

        attempt += 1


def menu():
    print(20*"-","Welcome to hot or cold",20*"-")
    time.sleep(1);
    print("This game will be about guessing the correct number.")
    time.sleep(1);
    print("The number will be between 1 to 100.")
    time.sleep(1);
    print("If the number you have guessed is far from the correct number it will be cold.")
    time.sleep(1);
    print("But the closer you get to the correct number the warmer it will be.")
    time.sleep(1);
    start = input("Are you ready? Enter Y or N: ")

    if start == "y" or start == "Y":
        start_game();

menu()