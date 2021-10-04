import json
import requests


sub = input("Choose your function:- \n1. Random anime quote\n2. 10 anime quotes \n3. Anime quote by anime name\n4. Anime quote by character name\n")

if sub == '1':
    
    response = requests.get("https://animechan.vercel.app/api/random")
    a = json.loads(response.content)
    print("Anime :"+a["anime"])
    print("\nCharacter :"+a["character"])
    print("\nQuote :"+a["quote"])
elif sub == '2':
    response = requests.get("https://animechan.vercel.app/api/quotes")
    a = json.loads(response.content)
    for items in range(len(a)):
        print("\n\n#"+str(items+1)+"Anime :"+a[items]["anime"])
        print("\n#"+str(items+1)+"Character :"+a[items]["character"])
        print("\n#"+str(items+1)+"Quote :"+a[items]["quote"])
elif sub == '3':
    aname = input("Anime name:")
    response = requests.get("https://animechan.vercel.app/api/quotes/anime?title="+aname)
    a = json.loads(response.content)
    print("Anime :"+a[0]["anime"])
    print("\nCharacter :"+a[0]["character"])
    print("\nQuote :"+a[0]["quote"])
elif sub == '4':
    chname = input("Character name:")
    response = requests.get("https://animechan.vercel.app/api/quotes/character?name="+chname)
    a = json.loads(response.content)
    print("Anime :"+a[0]["anime"])
    print("\nCharacter :"+a[0]["character"])
    print("\nQuote :"+a[0]["quote"])
else:
    print("invalid input, enter a number from 1 to 4.")