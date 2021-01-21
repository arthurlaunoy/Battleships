import string

class Coords:
    """
    Simple class that is used to translate coordinates of the battlefield into a
    more readable version.
    Example: (2, 1) becomes "B3"
        -> pair of coordinates
        -> a more readable version of this pair of coordinates
    """

    def __init__(self, x: int, y: int):
        alpha = "ABCDEFGHIJ"
        self.x = x
        self.y = y
        self.readable = alpha[y + 1] + str(x + 1)

    def getPair():
        return (self.x, self.y)

    def getReadable():
        return self.readable

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1
