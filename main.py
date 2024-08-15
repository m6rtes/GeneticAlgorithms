import random

deck =(2,3,4,5,6,7,8,9,10,10,10,10,11) # main deck tuple including aces (aces become 1 if user > 21)
dealer_hand = [] # dealer list to hold cars
user_hand = [] # user list to hold cards
    
def draw(): # function that will be called to draw a random card from the deck
    new_card = random.choice(deck)
    return new_card

def dealer_draw(user_total):
    if user_total < 21:
        while sum(dealer_hand) < 17:
            dealer_hand.append(draw())
    return dealer_hand

def blackjack(): # game fuction
    for i in range(2): # for loop to draw 2 cards to both the user and dealer
        user_hand.append(draw())
        dealer_hand.append(draw())
        
    print(f'User has: {user_hand}')
    print(f'Dealer has: {dealer_hand}')
    
    continue_game = True # will be used to terminate while loop
    
    while continue_game == True and sum(user_hand) < 21:
        drawing = input("Would you like to draw another card (y/n)       : ").lower()
        
        if drawing == 'y': # if users types y, it draws another card
            user_hand.append(draw())
            
            if 11 in user_hand and sum(user_hand) > 21: # aces (11's) get converted to 1's if > 21
                user_hand.remove(11)
                user_hand.append(1)
                
            print(f'User now has has: {user_hand}')
            print(f'Dealer has: {dealer_hand}')
            
        else:
            continue_game = False        
        
    dealer_draw(sum(user_hand)) # Function to draw card for dealer (if necessary)
                              
    print("~~~~~~ Final results ~~~~~~")
    print(f"User has {user_hand} for a total of {sum(user_hand)}")
    print(f"Dealer has {dealer_hand} for a total of {sum(dealer_hand)}")
    
    if sum(user_hand) > 21: #if statements check for bust, then draws, then checks for values between user/dealer 
        print("User busts! Dealer wins")
    elif sum(user_hand) == sum(dealer_hand):
        print("Draw")
    elif sum(dealer_hand) > sum(user_hand) and sum(dealer_hand) <= 21:
        print("Dealer wins")
    else:
        print("User wins")
    

# Main Game
print('________________________')
print("                      Welcome to Blackjack           ")
print("Blackjack is a card game where the user goes against the dealer.")
print("Your Goal is to draw cards to get closest to 21 points,")
print("however you don't want to go above 21 points because you will lose!")


play_game = False
while play_game == False:
    play = input("          Would you like to play?     (y/n)       :       ").lower()

    if play == "y":
        blackjack()
        play_game = True
    elif play == "n":
        print('_____________________')
        print("Goodbye")
        play_game = True
    else:
        print("You did not enter either 'y' or 'n'.")