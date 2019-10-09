# A simple Tic Tac Toe game. Can be played by two players via the console.
# Project made for Jose Portilla's Python Bootcamp on Udemy, modified by myself.
#
#
# Author: AgentNo
# Date Started: 8th October 2019
# Date Completed:

# board variable holds the current state of the board. Accessed through the functions.
board = {"1": '', "2": '', "3": '', "4": '', "5": '', "6": '', "7": '', "8": '', "9": ''}


def main():
    print('Welcome to Tic Tac Toe!')

    # Direct players to choose a piece
    pieces = ["X", "O"]
    # More efficient to deal with this in terms of indices rather than actual array content
    index = choosepiece()
    player1 = pieces[index]
    del pieces[index]
    player2 = pieces[0]
    print('Player 1 is ' + player1 + "and Player 2 is " + player2)
    print('Setting up game...')
    # Print the introduction of the game
    introduction()


    # won will record the win state of the game, full records the current state of board - both set to false initially
    won = False
    full = False
    # playerturn denotes the current player. True = Player 1, False = 0
    playerturn = True
    while not won or full:
        # Draw the board at the start of every iteration
        drawBoard()
        # Ask the user to place a marker. Pass arguments as appropriate
        if playerturn:
            placepiece("Player 1", player1)
        else:
            placepiece("Player 2", player2)

        # Now to check endgame conditions
        if checkWin():
            # If the player has won, exit the loop and end the game
            break
        elif isBoardFull():
            # If no win condition has been met and the board is full, end the game
            break
        else:
            # If neither condition has been met, reiterate the game
            continue
    print('Thank you for playing! Stopping game...')


# Allows the first player to choose their piece, X or O. Player 2 will be assigned what player 1 does not pick.
def choosepiece():
    while True:
        # Keep looping until the player chooses either X or O
        choice = input('Player 1, would you like to be X or O?')[0]
        if 'X' in choice.upper():
            # return the index of X
            return 0
        elif 'O' in choice.upper():
            # return the index of O
            return 1
        else:
            # Ask the player again until a satisfactory answer is obtained
            print('Invalid input - please enter X or O for your marker')
            continue


def introduction():
    demoboard = [range(0, 10)]
    print('In this game, you will take turns placing markers on the board. The board looks like this: \n')
    print(demoboard[0] + '|' + demoboard[1] + '|' + demoboard[2])
    print('-----')
    print(demoboard[3] + '|' + demoboard[4] + '|' + demoboard[5])
    print('-----')
    print(demoboard[6] + '|' + demoboard[7] + '|' + demoboard[8])
    print('Indicate where you wish to place your marker by entering the number of an empty square.')
    print('The winner is the first person to get three markers in a row horizontally, vertically or diagonally.')
    print('Player 1 will begin...')

def drawBoard():
    pass


def placepiece(player, piece):
    pass


def isempty(playerinput):
    pass


def checkWin():
    pass


def isBoardFull():
    pass


# Start the program at the main() function
if __name__ == "__main__":
    main()
