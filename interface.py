#Jason Padilla
#20502573
#ICS 32 Project2

import connectfour
import gamelogic

def begin_interface()->None:

    #Simply prints out a welcome message
    welcome_message()

    #Ask user if they want to start a game (y/n)
    response = ask_to_initate()

    #If reponse is y(True) than it will start the game
    if(response):
        start_game()
    else:
        print("Okay see you soon!")

def welcome_message():
    print("Hello, Welcome to Connect Four!")

def ask_to_initate() -> bool:
    #while this statement remains true it will continue to ask for an input
    #Y while start the game N will end it; anything else will restart
    while True:
        answer = input("Would you like to start a new game? (y/n) \n")
        if(answer.lower()) == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print("\nPlease enter a valid answer, either 'y' or 'n'")
            
def start_game() ->None:

    print("\nGame has started")
    #creates a brand new game state that can be modified
    game_state = connectfour.new_game_state()

    while True:
        #Outputs the game to the console
        gamelogic.display_board(game_state)
        
        if game_state.turn == 'R':
            print("\nRed Player: Make your move!")
        if game_state.turn == 'Y':
            print("\nYellow Player: Make your move!")

        column_number = gamelogic.ask_for_column()
        move_type = gamelogic.ask_for_type()

        #updates the game state with the new moves in place
        game_state = gamelogic.make_move(game_state,column_number,move_type)
        
        #checks to see if a player has won
        winning_player = connectfour.winning_player(game_state)

        if winning_player != " ":

            if winning_player == "R":
                print("\n### Red Is The Winner! ###")
            elif winning_player == "Y":
                print("\n### Yellow Is The Winner! ### ")
            gamelogic.display_board(game_state)
            print()
            break
    

    
if __name__ == "__main__":
    begin_interface()