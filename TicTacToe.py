# A simple Tic Tac Toe game in Python. Can be played by two players via the console.
# Project made as part of Jose Portilla's Python Bootcamp on Udemy.
#
#
# Author: AgentNo
# Date Started: 8th October 2019
# Date Completed: 17th October 2019

import sys  # required for exiting the game
import re  # validates input
import time # required to delay execution before starting game

# board variable holds the current state of the board. Accessed through function, global for ease of access.
board = {"1": '-', "2": '-', "3": '-', "4": '-', "5": '-', "6": '-', "7": '-', "8": '-', "9": '-'}


def main():
    print('Welcome to Tic Tac Toe!')

    # Direct players to choose a marker
    markers = ["X", "O"]
    # More efficient to deal with this in terms of indices rather than actual array content
    index = choosemarker()
    player1 = markers[index]
    del markers[index]
    player2 = markers[0]
    print('Player 1 is ' + player1 + " and Player 2 is " + player2)
    print('Setting up game...')
    # delay for dramatic effect
    time.sleep(2)
    # Print the introduction of the game
    introduction()

    # playerturn denotes the current player. True = Player 1, False = 0
    playerturn = True
    while True:
        # Draw the board at the start of every iteration
        drawboard()
        # Ask the user to place a marker. Pass arguments as appropriate
        if playerturn:
            validated = False
            while not validated:
                location = input('Player 1, where do you want to place a marker?')
                # validate the user's input
                if validateinput(location):
                    placemarker("Player 1", player1, location)
                    validated = True
                else:
                    print('Error - Please enter a number between 1 and 9 (inclusive)')

            # Check for win
            if checkwin(player1):
                # If Player 1 has won, print message and stop the game
                print('Player 1 got three in a row and wins the game!')
                print('Thank you for playing. Exiting the game...')
                sys.exit()
        else:
            validated = False
            while not validated:
                location = input('Player 2, where do you want to place a marker?')
                # validate the user's input
                if validateinput(location):
                    placemarker("Player 2", player2, location)
                    validated = True
                else:
                    print('Error - Please enter a number between 1 and 9 (inclusive')

            # Check for win
            if checkwin(player2):
                # If Player 2 has won, print message and stop the game
                print('Player 2 got three in a row and wins the game!')
                print('Thank you for playing. Exiting the game...')
                sys.exit()

        # Negate playerturn each time to switch between players
        playerturn = not playerturn

        # Now check if the board is full
        if isboardfull():
            # If no win condition has been met and the board is full, end the game
            print('Thank you for playing! Stopping game...')
            break
        else:
            # If neither condition has been met, reiterate the game
            continue


# Allows the first player to choose their piece, X or O. Player 2 will be assigned what player 1 does not pick.
def choosemarker():
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
    demoboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('In this game, you will take turns placing markers on the board. The board looks like this: \n')
    print(demoboard[0] + '|' + demoboard[1] + '|' + demoboard[2])
    print('-----')
    print(demoboard[3] + '|' + demoboard[4] + '|' + demoboard[5])
    print('-----')
    print(demoboard[6] + '|' + demoboard[7] + '|' + demoboard[8])
    print('')
    print('Indicate where you wish to place your marker by entering the number of an empty square.')
    print('The winner is the first person to get three markers in a row horizontally, vertically or diagonally.')
    print('Player 1 will begin...')


def drawboard():
    # print the current state of the board
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('')


def placemarker(player, piece, position):
    # Place the player's marker on the board as long as the space is empty
    if not isempty(position):
        # place the player's marker at the specified position
        board[position] = piece
        print(player + ' successfully placed an ' + piece + ' at position ' + str(position) + '.')
    else:
        # Skip this turn and let the other user take a turn
        print('Error - space is occupied. Skipping turn.')


def isempty(playerinput):
    # check to see if a particular space is occupied
    space = board[str(playerinput)]
    if space == '-':
        return False
    else:
        return True


def checkwin(marker):
    # The win conditions are three identical markers in a row (with indices), with leads to 7 win conditions:
    #   Horizontally (1,2,3 or 4,5,6 or 7,8,9) - consecutive squares
    #   Vertically (1,4,7 or 2,5,8 or 3,6,9) - every third square IF pos = 1, 2 or 3
    #   Diagonally (1,5,9 or 3,5,7) - every fourth square (1) or second square (3)

    # We will base the search off the player's marker - more efficient that writing code for both x and o
    # No other way except a really long if statement. Or a very long return statement. Personally, I think this looks more readable
    if board.get('1') == marker and board.get('2') == marker and board.get('3') == marker:
        # Player won horizontally
        return True
    elif board.get('4') == marker and board.get('5') == marker and board.get('6') == marker:
        # Player won horizontally
        return True
    elif board.get('7') == marker and board.get('8') == marker and board.get('9') == marker:
        # Player won horizontally
        return True
    elif board.get('1') == marker and board.get('4') == marker and board.get('7') == marker:
        # Player won vertically
        return True
    elif board.get('2') == marker and board.get('5') == marker and board.get('8') == marker:
        # Player won vertically
        return True
    elif board.get('3') == marker and board.get('6') == marker and board.get('9') == marker:
        # Player won vertically
        return True
    elif board.get('1') == marker and board.get('5') == marker and board.get('9') == marker:
        # Player won diagonally
        return True
    elif board.get('3') == marker and board.get('5') == marker and board.get('7') == marker:
        # Player won diagonally
        return True
    else:
        # Player has not got three in a row
        return False


def isboardfull():
    # Check to see if the board is full. Returns false if at least one space is empty, otherwise false
    for v in board.values():
        if v == '-':
            return False
    # If no spaces remain:
    print('The board is full with no clear winner. Game Ended.')
    return True


def validateinput(input):
    # Validate the user's input to ensure that only 1-9 has been input
    regex = re.compile(r'[1-9]')
    if bool(regex.search(str(input))):
        # If the input complies with the regex, return True
        return True
    else:
        return False


# point of entry at main()
if __name__ == "__main__":
    main()
