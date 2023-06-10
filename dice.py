class TwoDice:
    """This class is to simulate rolling two dice, and to get points.
    """
    def __init__(self):
        self.point1 = 0
        self.point2 = 0
        self.point = 0
        self.is_double = False

    def roll(self):
        import random
        random.seed()
        self.point1 = random.randint(1, 6)
        # random.seed()
        self.point2 = random.randint(1, 6)
        self.point = self.point1 + self.point2
        self.is_double = True if self.point1 == self.point2 else False

if __name__ == "__main__":
    my_twodice = TwoDice()
    my_twodice.roll()
    print(f"die1: {my_twodice.point1}")
    print(f"die2: {my_twodice.point2}")
    print(f"die: {my_twodice.point}")
    print(f"is double: {my_twodice.is_double}")
