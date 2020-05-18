
#global variables#

#Create a dictionary of 9 values that will represent the game board.
board = {
    "Top_left":" ", "Top_mid":" ", "Top_right":" ",
    "Mid_left":" ", "Mid_mid":" ", "Mid_right":" ",
    "Bottom_left":" ", "Bottom_mid":" ", "Bottom_right":" "}

board_positions = [
    "Top_left", "Top_mid", "Top_right",
    "Mid_left", "Mid_mid", "Mid_right",
    "Bottom_left", "Bottom_mid", "Bottom_right"]

game_on = True                 #sets a boolean variable that loops the game
player = "X"

#start of main code

#write a function to printout the board
def print_board():    #print the board values which are, of course, empty spaces.
    global board               #call the global variable to be used in the function
    print(board["Top_left"] + "|" + board["Top_mid"] + "|" + board["Top_right"])
    print("-+-+-")             # this will be a row seperator
    print(board["Mid_left"] + "|" + board["Mid_mid"] + "|" + board["Mid_right"])
    print("-+-+-")
    print(board["Bottom_left"] + "|" + board["Bottom_mid"] + "|" + board["Bottom_right"])
#call print_board() function to confirm that the board prints with no errors before proceeding to the next step

#write out the main function that starts the controls the game play.
def play_game():
    global game_on
    while game_on:
        print_board()          #the board must be printed everytime we need to play
        handle_turn()
        end_game()
        
#function that checks if the board is full and and ends the game
def end_game():
    global board
    global game_on
    if " " not in board.values(): #if no more empty space on the board, print the full board and end the game.
        print_board()
        print("Board Full!")
        game_on = False
    else:
        game_on
    

#define a function to start the game
def handle_turn():
    global board                #call all the global variables to be used in local scope
    global player
    global board_positions
    print(player, "'s turn")
    print("Positions:", board_positions)
    print("Choose one of the above positions to play")
    position = input()       
    while position not in board_positions or board[position] != " ":
        print("Invalid input or position")             #input exactly as on the board and in empty position.
        position = input() 
    board[position] = player
    if player == "X":
        player = "O"
    else:
        player = "X"
        

play_game()


