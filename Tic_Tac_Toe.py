
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
player = "X"                   #sets player X to start by default

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
#writing a program to check wins and draws
    if not game_on:
        if board["Top_left"] == board["Top_mid"] ==board["Top_right"]:    #wins in top row
            print(board["Top_left"], "wins")
        elif board["Mid_left"] == board["Mid_mid"] == board["Mid_right"]:  #wins in middle row
            print(board["Mid_left"], "wins")
        elif board["Bottom_left"] == board["Bottom_mid"] == board["Bottom_right"]:  #wins in bottom row
            print(board["Bottom_left"], "wins")
        elif board["Top_left"] == board["Mid_left"] == board["Bottom_left"]:         #wins in first column
            print(board["Top_left"], "wins")
        elif board["Top_mid"] == board["Mid_mid"] == board["Bottom_mid"]:             #wins in second column
            print(board["Top_mid"], "wins")
        elif board["Top_right"] == board["Mid_right"] == board["Bottom_right"]:        #wins in third column
            print(board["Top_right", "wins"])
        elif board["Top_left"] == board["Mid_mid"] == board["Bottom_right"]:           #wins in the diagonals
            print(board["Top_left"], "wins")
        else:
            print("It is a tie") 

#next step is to check for column wins  
        

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


