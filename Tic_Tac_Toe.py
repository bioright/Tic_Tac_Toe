
#global variables#

#Create a dictionary of 9 values that will represent the game board.
board = {
    "Top_left":" ", "Top_mid":" ", "Top_right":" ",
    "Mid_left":" ", "Mid_mid":" ", "Mid_right":" ",
    "Bottom_left":" ", "Bottom_mid":" ", "Bottom_right":" "
}

board_positions = ["Top_left", "Top_mid", "Top_right",
    "Mid_left", "Mid_mid", "Mid_right",
    "Bottom_left", "Bottom_mid", "Bottom_right"]

game_on = True                 #sets a boolean variable that loops the game
player = "X"

#start of main code

#write a function to printout the board
def print_board(dict_item):    #The function will take the dictionary assigned to board, as its argument
    global board               #call the global variable to be used in the function
    print(board["Top_left"] + "|" + board["Top_mid"] + "|" + board["Top_right"])
    print("-+-+-")             # this will be a row seperator
    print(board["Mid_left"] + "|" + board["Mid_mid"] + "|" + board["Mid_right"])
    print("-+-+-")
    print(board["Bottom_left"] + "|" + board["Bottom_mid"] + "|" + board["Bottom_right"])
#call print_board() function to confirm that the board prints with no errors before proceeding to the next step

#write out the main function that starts the controls the game play.
def play_game():
    print_board(board)                                     #the board must be printed everytime we need to play
    start_game()

#define a function to start the game
def start_game():
    global board
    global player
    global board_positions
    print(player, "'s turn")
    print("Positions:", board_positions)
    print("Choose one of the above positions to play")
    position = input()                                       #the input has to be exactly as spelt out on the board.
    board[position] = player
    if player == "X":
        player = "O"
    else:
        player = "X"
    

while game_on:                                               #putting the main function in a while loop
    play_game()


