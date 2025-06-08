import random

print("     __________________HANGMAN CHALLENGE__________________    ")
print()
def Game(Game_Start):
    if Game_Start.upper() == "Y":
        word_list=["CINEMA","GAME","FRIENDS"]
        l=random.choice(word_list)
        for i in l:
            print(" _ ",end="")
        print()
        print()
        
        game_over=False

        letter=[]
        lives=6
        draw= [
    """
     +---+
     |   |
     O   |
    /|\\ |
    / \\ |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\ |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\ |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """]
        
        while not game_over:
            Guess=input("Guess any Letter from the word to save the Man\n").upper()
            display=""

            
            

    
            for i in l:
                if i == Guess:
                    display += i
                    letter.append(i)
                    
                
                elif i in letter:
                    display += i
                else:
                    display+=" _ "
                    
            if Guess not in l:
                lives-=1
                if lives ==0:
                    game_over=True
                    print("You Lose.")
                
                    
            print(display)
            if " _ " not in display:
                game_over=True
                print("You Win.")

            print(draw[lives])
        
                
    else:
        print("Well, Bye!")
        










Game_Start=input("Wanna Play This Game 'Y' for YES 'N' for NO:\n")
Game(Game_Start)


