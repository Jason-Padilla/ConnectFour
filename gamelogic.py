#Jason Padilla
#20502573
#ICS 32 Project2
import connectfour

def display_board(game_state: connectfour.ConnectFourGameState) -> None:
    #Outputs the game state to the console
    print()

    #Outputs the numbers 1 - 7 at the top of the gameboard
    #Indicates the number of columns
    for col in range(connectfour.BOARD_COLUMNS):
        print(col+1,end=' ') #Plus 1 because the index starts at 0; "end" adds a space 
    print()

    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            #if the space is blank inside array representing the baord than output a "."
            if game_state.board[col][row] == connectfour.NONE:
                print(".", end = ' ')
            else:
                #else print out the value thats there
                print(game_state.board[col][row], end = " ")
        print()

def ask_for_column() -> int:
    
    #Initates a loop that will only exit once there is a valid move entered
    while True:
        chosen_col = input("\nChoose a column to drop/pop your piece: ")
        
        try:
            #converts the input to an int
            #if the value happens to be a non number then it will error and go to the except
            chosen_col = int(chosen_col)

            if chosen_col > 0 and chosen_col <= connectfour.BOARD_COLUMNS:
                return chosen_col

            #if it is a number but is not within range than it will also error
            else:
                print("[" + str(chosen_col) + "] is an invalid move, please try again." )
        
        except:
            print("[" + chosen_col + "] is an invalid input, please enter a number 1 - 7." )
def ask_for_type() -> str:

    #Initates a loop that will only exit once there is a valid type entered
    while True:
        chosen_type = input("Choose type of move (drop/pop): ")
        
        if(chosen_type.lower() == "drop"):
            return "drop"
        elif(chosen_type.lower() == "pop"):
            return "pop"
        else:
            print("\nPlease enter a valid move type.")

def make_move(game_state: connectfour.ConnectFourGameState, column_number: int, move_type: str) -> None:
    """
        Was going to initially add a While True at the top so that it would keep asking the 
        user to make a valid move. 
        But Edge Case: 
            if one of the columns is filled and they choose to drop than it would
            keep asking it to drop instead of going back to choose the type of move
    """
    try:
        if move_type == "drop":
            return connectfour.drop_piece(game_state,column_number-1)
        elif move_type == "pop":
            return connectfour.pop_piece(game_state,column_number-1)
    except:
        print("Invalid Move")
        return game_state



