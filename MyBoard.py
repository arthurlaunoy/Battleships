class Board:
    """
    Class holding all information related to a board:
        -> battlefield : the board itself.
        -> fleet : list of ship objects representing the fleet of boats that are still alive for the player using this board.
        -> 5 lists of coordinates representing the 5 locations of the ships on the board.
        -> name : the name of the board, it is the same as the player's name entered at the beginning of the game.
    """

    def __init__(self, name):
        self.battlefield = [[0 for x in range(10)] for z in range(10)]
        self.carrier = Carrier()
        self.battleship = Battleship()
        self.cruiser = Cruiser()
        self.patrolBoat = PatrolBoat()
        self.destroyer = Destroyer()
        self.fleet = [self.carrier, self.battleship, self.cruiser, self.patrolBoat, self.destroyer]
        self.playerName = name

    def position_ships_random(self):
        """
        This function fills the battlefield with random positions for the ships
        """

    def position_ships(self, coords):
        """
        This function fills the battlefield with positions taken from user input for the ships.

        param: list -> list of coordinates representing the locations of where the user want their ships.
        """

    def replaceXsByNumbers(self, battlefield, number, coords):
        """
        When a ship is drowned, this function is called to replace all the Xs in its location by a number
        representing the length of the ship. This function's purpose is solely so that the user can
        make the distinction between ships that they have already fully drowned and those they haven't.

        params: battlefield -> the battlefield on which the function replaces the characters.
                number -> the number by which the Xs will be replaced.
                coordinates -> list of coordinates representing a drowned ship.
        """
