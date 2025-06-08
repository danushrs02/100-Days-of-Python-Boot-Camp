print("----BLACK JACK-----")
import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(collection):
    total = 0
    if sum(collection) == 21 and len(collection) == 2:
        return 0
    
    if 11 in collection and sum(collection) > 21:
        collection.remove(11)
        collection.append(1)
        
    for value in collection:
        total += value
    return total

def compare(u_score,c_score):
    if u_score == c_score:
        return "DRAW |-_-|"
    elif u_score == 0:
        return "You Won"
    elif c_score == 0:
        return "You Lose, |'~'| "
    elif u_score > 21:
        return "You Went over, You Lose |'~'|"
    elif c_score > 21:
        return "Opponent Went Over, You Won"
    elif u_score > c_score:
        return "YOU WON"
    else:
        return "You Lose, |'~'|"
def play_game():
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card} Current score: {user_score}")
        print(f"Computer's First Card: {computer_card[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_card.append(deal_card())
            elif user_should_deal == 'n':
                is_game_over = True
            else:
                print("Wrong Input.")
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
        
    print(f"Your Cards: {user_card} , Your Score: {user_score}")
    print(f"Opponent Cards {computer_card}, Computer Score: {computer_score}")

    print(compare(user_score,computer_score))

while input("Do you wanna play BLACK JACK 'y' for yes 'n' for 'n'").lower() == 'y':
    print("\n" * 200)
    play_game()
    
        
