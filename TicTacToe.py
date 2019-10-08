# A simple Tic Tac Toe game. Can be played by two players via the console.
# Project made for Jose Portilla's Python Bootcamp on Udemy, modified by myself.
#
#
# Author: AgentNo
# Date Started: 8th October 2019
# Date Completed:

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
    print('Player 1, are you ready to start?')


def choosepiece():
    while True:
        # Keep looping until the player chooses either X or O
        choice = input('Player 1, would you like to be X or O?')[0]
        if 'X' in choice.upper():
            # return the index of X - 0
            return 0
        elif 'O' in choice.upper():
            # return the index of O - 1
            return 1
        else:
            # Ask the player again until a satisfactory answer is obtained
            print('Invalid input - please enter X or O for your marker')
            continue

