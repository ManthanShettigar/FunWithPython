name = input("What is your name? ")

while True:
    prompt = input("Enter a statement or RETURN to close: ")

    if not prompt:
        break

    check_str = name + prompt

    if hash(check_str.lower()) % 2 == 0:
        print("That is a filthy lie!")
    else:
        print("That is the truth!")
        
