#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Will hold our game data
array = ["*", "*", "*",
         "*", "*", "*",
         "*", "*", "*"]
# Initializing the values and setting the boolean so we can determine if the game is over
# as long it's true the program won't exit
winner = None
current = "O"
Game_Running = True



def Start_game():
    # to display the game
    display_array()

    # This is simplifying the logic of game it give the O we initialize at the beginning the first turn
    # than if the game is over and that is by going thru the function we defined that has win/tie
    # if the game is not over the switch function will be be called
    while Game_Running:

        player(current)

        check_if_game_over()

        switch_player()
    # printing the winner and exiting the loop
    if winner == "X" or winner == "O":
        print(winner + " won.")
    # printing tie if the array is filled without a diagonal or row or column win
    elif winner == None:
        print("Tie.")


# Display the game to the screen
def display_array():
    print("\n")
    print(array[0] + " | " + array[1] + " | " + array[2] + "     1 | 2 | 3")
    print(array[3] + " | " + array[4] + " | " + array[5] + "     4 | 5 | 6")
    print(array[6] + " | " + array[7] + " | " + array[8] + "     7 | 8 | 9")
    print("\n")


# this how we start the game by giving the user the spots where he can place his piece
def player(Player):
    print(Player + "'s turn.")
    # Get Spot from player
    Spot = input("Choose a Spot from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while Spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            Spot = input("Choose a Spot from 1-9: ")

        # we take 1 because our index start from 0
        Spot = int(Spot) - 1

    # it exit this loop valid has to be true and it will be true only if the spot taken is *
    # that mean it won't overwrite other pieces
        if array[Spot] == "*":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the array
    array[Spot] = Player

    # Show the game
    display_array()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():
    # we set it to global variables so we can use it everytime
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
    # Set global variables
    global Game_Running
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = array[0] == array[1] == array[2] != "*"
    row_2 = array[3] == array[4] == array[5] != "*"
    row_3 = array[6] == array[7] == array[8] != "*"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        Game_Running = False
    # Return the winner
    if row_1:
        return array[0]
    elif row_2:
        return array[3]
    elif row_3:
        return array[6]
        # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns():
    # Set global variables
    global Game_Running
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = array[0] == array[3] == array[6] != "*"
    column_2 = array[1] == array[4] == array[7] != "*"
    column_3 = array[2] == array[5] == array[8] != "*"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        Game_Running = False
    # Return the winner
    if column_1:
        return array[0]
    elif column_2:
        return array[1]
    elif column_3:
        return array[2]
        # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global Game_Running
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = array[0] == array[4] == array[8] != "*"
    diagonal_2 = array[2] == array[4] == array[6] != "*"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        Game_Running = False
    # Return the winner
    if diagonal_1:
        return array[0]
    elif diagonal_2:
        return array[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_for_tie():
    # Set global variables
    global Game_Running
    # If board is full
    if "*" not in array:
        Game_Running = False
        return True
    # Else there is no tie
    else:
        return False


# Flip the current player from X to O, or O to X
def switch_player():
    global current
    # If the current player was X, make it O
    if current == "X":
        current = "O"
    # Or if the current player was O, make it X
    elif current == "O":
        current = "X"


# Start a game of tic tac toe
Start_game()


# %%
