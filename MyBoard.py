from MyCoords import Coords
from MyShips import *
import random

class Board:
    """
    Class holding all information related to a board:
        -> battlefield : the board itself.
        -> fleet : list of ship objects representing the fleet of boats that are still alive for the player using this board.
        -> 5 lists of coordinates representing the 5 locations of the ships on the board.
        -> name : the name of the board, it is the same as the player's name entered at the beginning of the game.
    """

    def __init__(self, name, random: bool, coords = None):
        self.battlefield = [[0 for x in range(10)] for z in range(10)]
        if random:
            coords_list = self.get_ships_position(random, coords)
        else:
            coords_list = coords
        self.carrier = Carrier(coords_list[0])
        self.battleship = Battleship(coords_list[1])
        self.cruiser = Cruiser(coords_list[2])
        self.destroyer = Destroyer(coords_list[3])
        self.fleet = [self.carrier, self.battleship, self.cruiser, self.destroyer]
        self.playerName = name

    def get_random_ships_position(self):
        """
        This function paints the battlefield at the locations of the ships and
        creates a random list of list of coordinates that will be used to locate the fleet.

        return: list -> random list of list of coordinates that will be used to locate the fleet.
        """

        directions = ['U', 'D', 'L', 'R']
        coords_list = []

        for i in range(4):
            random_pos = getGridPositionFromNumber(random.randrange(1, 100))
            while getBattlefieldSquareFromCoords(random_pos) != 0:
                random_pos = getGridPositionFromNumber(random.randrange(1, 100))
            random.shuffle(directions)
            for d in directions:
                if isPlacementPossible(i, random_pos, d):
                    ship_coords = paint_battlefield(d, random_pos, i)
                    coords_list.append(ship_coords)

        return coords_list

    def paint_battlefield(direction: str, coords: Coords, nb_tiles: int):
        """
        This function first paints the battlefield at the location of the ship and
        also creates a list of Coords corresponding to that ship.

        param: str -> the direction in which we paint the battlefield.
               Coords -> the starting point of the ship.
               nb_tiles -> the number of tiles to paint.

        return: list -> list of coordinates corresponding to a ship.
        """

        ship_coords = []
        dummy_coords = coords

        for i in range(nb_tiles):
            setBattlefieldSquareFromCoords(dummy_coords, "X")
            ship_coords.append(dummy_coords)
            if direction == 'U':
                dummy_coords.move_up()
            if direction == 'D':
                dummy_coords.move_down()
            if direction == 'L':
                dummy_coords.move_left()
            else:
                dummy_coords.move_right()

        return ship_coords

    def isPlacementPossible(ship_size: int, coords: Coords, direction: str):
        """
        Checks if it it possible to place a ship at the given coordinates, considering
        the given direction and ship size.

        params: int -> the size of the ship.
                Coords -> the starting point of the ship.
                str -> the direction in which to check for obstacles.

        return: bool -> True if the placement is possible, False otherwise.
        """

        pos = coords.getPair()
        i = 0
        dummy_coords = coords
        while getBattlefieldSquareFromCoords(dummy_coords) == 0 and i < ship_size:
            if direction == 'U':
                dummy_coords.move_up()
            if direction == 'D':
                dummy_coords.move_down()
            if direction == 'L':
                dummy_coords.move_left()
            else:
                dummy_coords.move_right()
            i += 1

        return (i == ship_size)


    def getGridPositionFromNumber(n: int) -> Coords:
        """
        Given a number between 1 and 100, gets the corresponding position in a
        10 by 10 grid.

        param: int -> the number between 1 and 100.

        return: Coords -> the position on the board corresponding to the given number.
        """

        o = n // 10
        a = n % 10

        return Coords(a - 1, o - 1)

    def getBattlefieldSquareFromCoords(coords: Coords):
        """
        Given coordinates, get the content of the corresponding square on the board.

        param: Coords -> the given coordinates.

        return: int -> the content of the square.
        """

        x, y = coords.getPair()

        return self.battlefield[x][y]

    def setBattlefieldSquareFromCoords(coords: Coords, content):
        """
        Given coordinates, set the content of the corresponding square on the board.

        param: Coords -> the given coordinates.
               content -> what to set in the square.

        return: int -> the content of the square.
        """

        x, y = coords.getPair()

        self.battlefield[x][y] = content

    def replaceXsByNumbers(self, coords):
        """
        When a ship is drowned, this function is called to replace all the Xs in its location by a number
        representing the length of the ship. This function's purpose is solely so that the user can
        make the distinction between ships that they have already fully drowned and those they haven't.

        params: coords -> list of Coords representing a drowned ship.
        """

        ship_size = len(coords)
        for x in coords:
            if getBattlefieldSquareFromCoords(x) == 'X'
                setBattlefieldSquareFromCoords(x, ship_size)
