from guietta import _, Gui, Quit
import random

gui= Gui(
    [_,"Deck of Card",_],
    [_, ["Shuffle"], _],
    [_, 'number', _],
    [_,'suite',_],
    [_, Quit, _]
    )

def shuffle(gui):
    n= random.randint(1,13)
    if (n== 1):
        n="Ace"
    elif(n== 11):
        n="Jack"
    elif(n==12):
        n="Queen"
    elif(n==13):
        n="King"
    else:
        pass
    c= random.randint(1,4)
    if(c==1):
        c= "Spades"
    elif(c==2):
        c= "Hearts"
    elif(c==3):
        c= "Diamonds"
    elif(c==4):
        c= "Clubs"
    else:
        pass
    gui.suite= c
    gui.number= n

gui.Shuffle=shuffle

gui.run()
