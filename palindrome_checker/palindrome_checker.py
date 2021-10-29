
if __name__ == "__main__":
    import re

    word = input("Enter the word you think is a palindrome: ")

    #Remove spaces and punctuation so phrases work as well
    clean_word = re.sub(r'\W', "", word)

    if clean_word.lower() == clean_word[::-1].lower():
        print("That's a palindrome!")
    else:
        print("Not a palindrome")
