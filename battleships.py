from MyBoard import Board
import random

def drawBoards(board1: Board, board2: Board):
    """
    Draws the boards at each turn of the game.

    params: board1 -> first board, drawn on the left of the terminal, representing the current user's board.
            board2 -> second board, drawn on the right of the terminal, representing the the opponent's board.
    """

def checkUserInputCoordinates(coords: str) -> bool:
    """
    Checks if the coordinates the input by the user are in the grid.

    param: str -> coords input by the user.

    return: bool -> True if coords are correct and False otherwise.
    """

def checkStateOfSquare(coords: str) -> int:
    """
    Return the state of the square guessed by the player.

    param: str -> coords input by the user.

    return: int -> a number representing the state of the square ->
                        -> 1 if it is Water
                        -> 2 if it is a ship the user just discovered
                        -> 3 if it is a ship already guessed
    """

def isGameOver(fleet: list) -> int:
    """
    Checks if the game is over.

    param: list -> list of list of coordinates representing the fleet of boats that are still alive for each player.

    return: int -> a number representing the state of the whole game ->
                        -> 1 if the game is not over.
                        -> 2 if player 1 won the game.
                        -> 3 if player 2 or the Computer won the game.
    """

def coinflip(stand: str) -> int:
    """
    A function doing a coinflip at the beginning of the game to decide which player will go first.

    param: str -> a letter representing heads or tails.

    return: int -> a number representing the player that will go first ->
                        -> 1 for player 1
                        -> 2 for player 2
    """

    faces = ['H', 'T']
    res = random.random(faces)
    if res == stand:
        return 1
    else:
        return 2

# TODO: function at end of game -> nb of turns and/or play again ? for example

def main():
    # Welcome text
    # ask user if the game will be played with 2 players or 1 player against my AI
    # ask for players names
    # random placement or user placement of ships ?
    # coinflip to know who goes first
    # Start game loop:
        # draw both boards (both blank on turn 1)
        # prompt coords from current player
        # check state of square
        # paint square according to the result of line above
        # check if game is over
        # if game is not over, switch player turn if the current user played in the water
        # if game is over, get out of loop
    # call after-game function for stats and possibility to play again
