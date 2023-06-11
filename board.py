"""this file to make paly board.
"""



class Board:
    def __init__(self, name):
        import os
        self.name = name
        self.image_loc = os.path.join("pic", r"board_" + name + r".png")