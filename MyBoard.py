class Board:
    """
    Class holding all information related to a board:
        -> battlefield : the board itself.
        -> fleet : list of list of coordinates representing the fleet of boats that are still alive for the player using this board.
        -> 5 lists of coordinates representing the 5 locations of the ships on the board.
        -> name : the name of the board, it is the same as the player's name entered at the beginning of the game.
    """

    def __init__(self, name):
        self.fleet =
        self.battlefield =
        self.carrier_coords =
        self.battleship_coords =
        self.cruiser_coords =
        self.patrolBoat_coords =
        self.destroyer_coords =
        self.playerName = name

    def position_ships_random(self):

    def position_ships(self, coords):

    def replaceXsByNumbers(self, battlefield, number, coords):
        """
        When a ship is drowned, this function is called to replace all the Xs in its location by a number
        representing the length of the ship. This function's purpose is solely so that the user can
        make the distinction between ships that they have already fully drowned and those they haven't.

        params: battlefield -> the battlefield on which the function replaces the characters.
                number -> the number by which the Xs will be replaced.
                coordinates -> list of coordinates representing a drowned ship.
        """
