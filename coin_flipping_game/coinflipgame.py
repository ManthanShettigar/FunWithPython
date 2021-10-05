import random
import time
print("-------------------------- COIN FLIPPING GAME -----------------------------")
choice = input("Make your choice~ (heads or tails): ")
number = random.randint(1,2)
if number == 1:
    result = "heads"
elif number == 2:
    result = "tails"
print("-------------------------------- DECIDING ----------------------------------")
time.sleep(2)
if choice == result:
    print("WOOOOO WELL DONE YOU WON!!!! The coin you flipped were", result)
else:
    print("Awww man, you lose. But you can run the script again y'know, The coin you flipped were", result)
print("Thanks for playing the coin flipping game!!!")