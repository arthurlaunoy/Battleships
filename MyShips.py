from MyCoords import Coords

class Ship:
    """
    Generic ship class.
    """

    def __init__(self, coords: Coords):
        self.coords = coords
        self.main_coord = getMainCoord()

    def checkShipConsistency(self):
        """
        Checks if the shape of the ship is correct. This fucnction will mainly be
        used in the case where the user inputs its own coordinates for their ships.
        """
        return True

    def getMainCoord(self):
        """
        Get the 'main' coordinate of a boat from its list of coordinates. The main
        coordinate is the leftmost or the topmost coordinate for ships that have 'straight line'
        kind of shape. For the other ship, we take the center point as the main coordinate.
        """

class Carrier(Ship):
    """
    Carrier ship class. A Carrier is a linear ship, 5 cases long.
    """

    def checkShipConsistency(self) -> bool:
        c = [x.getPair() for x in self.coords]

        if len(c) != 5:
            return False
        a = [p[1] for p in c]
        o = [p[0] for p in c]

        return (len(set(a)) == 1 or len(set(o)) == 1)

class Battleship(Ship):
    """
    Battleship ship class. A Battleship is a linear ship, 4 cases long.
    """

    def checkShipConsistency(self):
        c = [x.getPair() for x in self.coords]
        if len(c) != 4:
            return False
        a = [p[1] for p in c]
        o = [p[0] for p in c]

        return (len(set(a)) == 1 or len(set(o)) == 1)

class Cruiser(Ship):
    """
    Cruiser ship class. A Cruiser is a linear ship, 3 cases long.
    """

    def checkShipConsistency(self):
        c = [x.getPair() for x in self.coords]
        if len(c) != 3:
            return False
        a = [p[1] for p in c]
        o = [p[0] for p in c]

        return (len(set(a)) == 1 or len(set(o)) == 1)

class Destroyer(Ship):
    """
    Destroyer ship class. A Destroyer is a linear ship, 2 cases long.
    """

    def checkShipConsistency(self):
        c = [x.getPair() for x in self.coords]
        if len(c) != 2:
            return False
        a = [p[1] for p in c]
        o = [p[0] for p in c]

        return (len(set(a)) == 1 or len(set(o)) == 1)

class PatrolBoat(Ship):
    """
    Patrol Boat ship class. A Patrol Boat is a T-shaped ship, with a total of 4 cases.
    """

    def checkShipConsistency(self):
        c = [x.getPair() for x in self.coords]
        if len(c) != 4:
            return False

        m = self.main_coord.getPair()
        for pair in c:
            if pair != m:
                if pair[1] == m[1]:
