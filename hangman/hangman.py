import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while game_is_finished!=True:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life, lives remain = {lives}.")
        if lives == 0:
            game_is_finished = True
            print("You lose.")
        if lives == 2:
           print("do you want a hint ? if yes you'll loose a live")
           res = input("y-for yes and n-for no")
           if res == 'y' or res == 'Y':
             lives-=1
             pos = int(input("which position ans you want?"))
             hint = chosen_word[pos]
             print(hint)
             print("lives remain ",lives)
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])


print("the word was ",chosen_word)